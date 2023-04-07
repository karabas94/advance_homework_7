from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Publisher, Store
from django.db.models import Count, Avg
from .forms import ReminderForm


def index(request):
    return render(request, 'library/index.html')


def author_list(request):
    authors = Author.objects.prefetch_related('book_set').annotate(num_books=Count('book')).all()
    return render(request, 'library/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author.objects.prefetch_related('book_set').all(), pk=pk)
    avg_rating = author.book_set.all().aggregate(Avg('rating'))['rating__avg']
    return render(request, 'library/author_detail.html', {'author': author, 'avg_rating': avg_rating})


def book_list(request):
    books = Book.objects.prefetch_related('authors').annotate(num_authors=Count('authors')).all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book.objects.select_related('publisher').prefetch_related('authors').all(), pk=pk)
    num_authors = book.authors.all().aggregate(Count('id'))['id__count']
    return render(request, 'library/book_detail.html', {'book': book, 'num_authors': num_authors})


def publisher_list(request):
    publishers = Publisher.objects.prefetch_related('book_set').annotate(num_books=Count('book')).all()
    return render(request, 'library/publisher_list.html', {'publishers': publishers})


def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher.objects.prefetch_related('book_set'), pk=pk)
    avg_price = publisher.book_set.all().aggregate(Avg('price'))['price__avg']
    return render(request, 'library/publisher_detail.html', {'publisher': publisher, 'avg_price': avg_price})


def store_list(request):
    stores = Store.objects.prefetch_related('books').annotate(num_books=Count('books')).all()
    return render(request, 'library/store_list.html', {'stores': stores})


def store_detail(request, pk):
    store = get_object_or_404(Store.objects.prefetch_related('books'), pk=pk)
    avg_pages = store.books.aggregate(Avg('pages'))['pages__avg']
    return render(request, 'library/store_detail.html', {'store': store, 'avg_pages': avg_pages})


def reminder(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            reminder_form.save()
            return redirect('success')
    else:
        reminder_form = ReminderForm()
    return render(request, 'library/reminder.html', {'reminder_form': reminder_form})


def success(request):
    return render(request, 'library/success.html')
