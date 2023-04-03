from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Publisher, Store


def index(request):
    return render(request, 'library/index.html')


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'library/publisher_list.html', {'publishers': publishers})


def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'library/publisher_detail.html', {'publisher': publisher})


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'library/store_list.html', {'stores': stores})


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'library/store_detail.html', {'store': store})
