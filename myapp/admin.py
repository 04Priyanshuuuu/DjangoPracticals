from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    ordering = ('title',)


admin.site.register(Book, BookAdmin)
