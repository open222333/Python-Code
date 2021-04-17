from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    # 調用 render() 函數來創建並返回HTML頁面作為響應（此快捷功能包裝了許多其他函數，從而簡化了這種非常常見的用例）。
    # 它以原始 request 物件 (一個 HttpRequest)
    # 帶有數據佔位符的HTML模板以及上下文 context 變量包含將插入到這些佔位符中的數據的Python字典）為參數。
    return render(request, 'index.html', context=context)

# 通用view將查詢數據庫，以獲取指定模型（Book）的所有記錄


class BookListView(generic.ListView):
    model = Book
    # 添加屬性
    context_object_name = 'my_book_list'
    # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5]
    # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'
    # Specify your own template name/location

    # 覆寫某些類別方法
    def get_queryset(self):
        # 列出其他用戶閱讀的前5本書，而不是列出所有書本。
        return Book.objects.filter(title_icontains='war')[:5]

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is jut some data'
        return context
