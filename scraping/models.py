from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    born = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote
