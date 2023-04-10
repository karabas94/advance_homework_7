from django.shortcuts import render
from .models import Author, Quote


def index(request):
    quotes = Quote.objects.all()
    return render(request, 'scraping/index.html', {'quotes': quotes})


def quotes_by_author(request, author_id):
    author = Author.objects.get(id=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'scraping/quotes_by_author.html', {'author': author, 'quotes': quotes})
