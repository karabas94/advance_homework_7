from django.contrib import admin

from .models import Author, Publisher, Book, Store


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']
    fieldsets = [
        ('Author', {'fields': [('name', 'age'), ]}),
    ]


class PublisherInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 50
    inlines = [PublisherInline]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']
    list_filter = ['pubdate']
    search_fields = ['name']
    date_hierarchy = 'pubdate'
    filter_horizontal = ['authors']
    raw_id_fields = ('publisher', )
    list_per_page = 50


@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_vertical = ['books']
    list_per_page = 50
