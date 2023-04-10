from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Author, Quote
from django.core.mail import send_mail


@shared_task
def parse_quote():
    quotes_saved = 0
    page_number = 1
    while True:
        r = requests.get(f"https://quotes.toscrape.com/page/{page_number}/")
        soup = BeautifulSoup(r.text, 'html.parser')
        for quote in soup.findAll('div', {'class': 'quote'}):
            text = quote.find('span', {'class': 'text'}).string
            author_name = quote.find('small', {'class': 'author'}).string
            author_url = quote.find('small', {'class': 'author'}).find_next('a')['href']
            author_link = requests.get('https://quotes.toscrape.com' + author_url)
            author_soup = BeautifulSoup(author_link.text, 'html.parser')
            born_date = author_soup.find('span', {'class': 'author-born-date'}).string
            born_location = author_soup.find('span', {'class': 'author-born-location'}).string
            born = born_date + " " + born_location
            author, created = Author.objects.get_or_create(name=author_name, born=born)
            quote, created = Quote.objects.get_or_create(quote=text, author=author)
            if created:
                quotes_saved += 1
            if quotes_saved == 5:
                return
        next_page = soup.find('li', {'class': 'next'})
        if not next_page:
            send_mail(
                'Parsing finished',
                'No more quotes',
                'admin@admin.com',
                fail_silently=False,
                recipient_list=['too@gmail.com']
            )
            break
        page_number += 1
