from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# 先將模型導入，再呼叫 admin.site.register 函式來註冊每個模型。
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
