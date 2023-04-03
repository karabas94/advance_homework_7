from django.core.management.base import BaseCommand
from library.models import Author, Publisher, Book, Store
from random import randint, choice
import random
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create library'

    def handle(self, *args, **options):
        # create 100 author
        authors = [Author(name=fake.name(), age=randint(20, 80)) for _ in range(100)]
        Author.objects.bulk_create(authors)

        # create 10 publisher
        publishers = [Publisher(name=f'Publisher{index}') for index in range(1, 11)]
        Publisher.objects.bulk_create(publishers)

        # create 1000 books
        books = []
        for index in range(1000):
            book = Book(
                name=f"Book {index}",
                pages=randint(100, 1000),
                price=Decimal(random.uniform(25, 300)),
                rating=random.uniform(0, 10),
                publisher=choice(publishers),
                pubdate=timezone.now() - timedelta(days=randint(0, 1000)),
            )
            book.save()
            book.authors.set(choice(authors) for _ in range(randint(1, 4)))
            books.append(book)

        # create 10 stores
        stores = []
        for i in range(10):
            store = Store(
                name=f"Store {i}",
            )
            store.save()
            store.books.set(Book.objects.order_by('?')[:randint(50, 200)])
            stores.append(store)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(authors)} authors, {len(publishers)} publishers, '
                                             f'{len(books)} books and {len(stores)} stores.'))
