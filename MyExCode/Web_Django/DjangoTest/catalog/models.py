from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
import uuid  # Required for unique book instances

# 書籍類型模型 (Genre model)


class Genre(models.Model):
    """Model representing a book genre."""
    # 這個模型是用來儲存書籍類型的資訊 — 例如：該本書是否為科幻小說、羅曼史、軍事歷史等。
    name = models.CharField(
        max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# 書本模型 (Book model)


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    # 這個 Book 模型一般來說代表一個可用書本的所有資訊，但並非包含特定的物理實例(physical instance)
    # 或者副本資訊(copy)，此模型使用 CharField 來表示書的 title 和 isbn (國際標準書號)(note how the
    # isbn specifies its label as "ISBN" using the first unnamed parameter
    # because the default label would otherwise be "Isbn").，另外此模型使用
    # TextField 來存 summary ，因為此文本可能會很長。
    title = models.CharField(max_length=200)
    # 作者(author)被宣告為外鍵(ForeignKey)，因此每本書只會有一名作者，但一名作者可能會有多本書
    # (實際上，一本書可能會有多名作者，不過這個案例不會有，所以在別的例子這種作法可能會有問題)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    # Foreign Key used because book can only have one author, but authors can
    # have multiple books
    # Author as a string rather than object because it hasn't been declared
    # yet in the file.
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(
        'ISBN', max_length=13, help_text='13 Character <a \
            href="https://www.isbn-international.org/content/what-isbn">\
            ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can
    # cover many genres.
    # Genre class has already been defined so we can specify the object above.
    # 「書籍類別」(genre)是一個 ManyToManyField ，因此一本書可以有很多書籍類別，而一個書結類別也能夠對應到很多本書。
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    # 回傳一個可以被用來存取該模型細節紀錄的 URL (要讓其有效運作，我們必須定義一個 URL 的映射，我們將其命名為 book-detail
    # ，另外還得定義一個關聯示圖(view)與模板(template) )。

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in
         Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


# 書本詳情模型 (BookInstance model)


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed
    from the library)."""
    # BookInstance 模型表示一個特定的書籍副本(可會被某人借走)，
    # 並且包含如「副本是否可用」、「預計歸還日期」、「版本說明」或「版本細節」等資訊，
    # 還有一個在圖書館中唯一的 id 。
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular \
                              book across whole library')
    # UUIDField 被用來將 id 字段再這個模型中設定為 primary_key，這類別的字段會分配一個全域唯一的值給每一個
    # 實例(instance)，也就是任何一本你能在圖書館找到的書。
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    # DateField 會被用來設定 due_back 的日期(紀錄書本何時會被歸還，可再被使用，或者是否正在保養期)，
    # 這個字段允許 blank 或 null 值，而當元數據模型 (Class Meta)收到請求(query)時
    # 也會使用此字段來做資料排序。

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    #  status 是一個 CharField 字段，用來定義一個選項列表。你可以看到，我們定義了一個包含「鍵-值對元組」
    # 的元組(tuple) 並使其成為選項的參數，鍵-值對中的值會陳列出來並可以被使用者選擇，當選項被選定後，鍵
    # (key)也會被儲存下來。我們也設定了預設的鍵值為 "m" (maintenance)
    # 用來表示當每本書在初始創造還未放上書架時是不可被使用的。
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        # 從 Python3.6 開始，你可以使用「字串插值語法」(又稱做 f-string)
        return f'{self.id} ({self.book.title})'

# 作者模型(Author model)


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    # 反轉 author-detail 的URL映射，來獲得顯示單個作者的URL。
    # 無法直接在 list_display 中指定「書籍類別」(genre field)字段，因為它是一個 ManyToManyField
    # (多對多字段)，因為如果這樣做會造成很大的資料庫讀寫「成本」，所以 Django 會預防這樣的狀況發生，因此，取而代之，我們將定義一個
    # display_genre 函式以「字串」形式得到書籍類別。

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


# 語言模型(Language model)
class Language(models.Model):
    name = models.CharField(
        max_length=200, help_text='Input the Language of book')

    def __str__(self):
        return self.name
