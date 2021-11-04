from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# 先將模型導入，再呼叫 admin.site.register 函式來註冊每個模型。
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
# Define the admin class
# 註冊一個 模型管理 類別 (ModelAdmin class)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# 現在我們要創造並註冊新的模型；為了達到示範的目的，我們會使用 @register
# 裝飾器替代先前做法來註冊模型(這跟 admin.site.register() 的語法做的事情完全一樣)
# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
