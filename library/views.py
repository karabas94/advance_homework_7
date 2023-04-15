from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Publisher, Store
from django.db.models import Count, Avg
from .forms import ReminderForm
from .tasks import send_reminder
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def index(request):
    return render(request, 'library/index.html')


def author_list(request):
    authors = Author.objects.prefetch_related('book_set').annotate(num_books=Count('book')).all()
    return render(request, 'library/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(
        Author.objects.annotate(avg_rating=Avg("book__rating")).prefetch_related('book_set').all(), pk=pk)
    avg_rating = author.avg_rating
    return render(request, 'library/author_detail.html', {'author': author, 'avg_rating': avg_rating})


class BookListView(ListView):
    model = Book
    paginate_by = 10
    queryset = Book.objects.prefetch_related('authors').annotate(num_authors=Count('authors')).all()

# def book_list(request):
#     books = Book.objects.prefetch_related('authors').annotate(num_authors=Count('authors')).all()
#     return render(request, 'library/book_list.html', {'books': books})


class BookDetailView(DetailView):
    model = Book

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('publisher').annotate(num_authors=Count('authors'))
        return queryset


def publisher_list(request):
    publishers = Publisher.objects.prefetch_related('book_set').annotate(num_books=Count('book')).all()
    return render(request, 'library/publisher_list.html', {'publishers': publishers})


def publisher_detail(request, pk):
    publisher = get_object_or_404(
        Publisher.objects.prefetch_related('book_set').annotate(price__avg=Avg("book__price")), pk=pk)
    avg_price = publisher.price__avg
    return render(request, 'library/publisher_detail.html', {'publisher': publisher, 'avg_price': avg_price})


def store_list(request):
    stores = Store.objects.prefetch_related('books').annotate(num_books=Count('books')).all()
    return render(request, 'library/store_list.html', {'stores': stores})


def store_detail(request, pk):
    store = get_object_or_404(Store.objects.prefetch_related('books').annotate(price__avg=Avg("books__price")), pk=pk)
    avg_pages = store.price__avg
    return render(request, 'library/store_detail.html', {'store': store, 'avg_pages': avg_pages})


def reminder(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            email = reminder_form.cleaned_data['email']
            text = reminder_form.cleaned_data['text']
            datetime = reminder_form.cleaned_data['datetime']
            send_reminder.apply_async(args=[email, text], eta=datetime)
            return redirect('library:success')
    else:
        reminder_form = ReminderForm()
    return render(request, 'library/reminder.html', {'reminder_form': reminder_form})


def success(request):
    return render(request, 'library/success.html')
