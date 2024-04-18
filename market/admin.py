from django.contrib import admin
from .models import Author, Category, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'author', 'category', 'price', 'cover_type']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
