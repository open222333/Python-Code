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


def book_detail_view(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist as Http404:
        raise Http404('Book does not exist')

    # from django.shortcuts import get_object_or_404
    # book = get_object_or_404(Book, pk=primary_key)

    return render(request, 'book_detail.html', context={'book': book})


def testpage(request):
    book_test = Book.objects.all()
    context = {'book_test': book_test}
    return render(request, 'testpage.html', context=context)

# 通用view將查詢數據庫，以獲取指定模型（Book）的所有記錄


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # 添加屬性
    context_object_name = 'books'
    # # your own name for the list as a template variable
    # queryset = Book.objects.all()
    # # Get 5 books containing the title war
    template_name = 'book_list.html'
    # # Specify your own template name/location
    # # 覆寫某些類別方法

    # def get_queryset(self):
    #     # 列出其他用戶閱讀的前5本書，而不是列出所有書本。
    #     return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist as Http404:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})
