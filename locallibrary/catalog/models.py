from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Модель представляет жанр книги"""
    name = models.CharField(max_length=200, help_text='Введите жанр книги')

    def __str__(self):
        return self.name


class Book(models.Model):
    """Модель представляет книгу"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Введите краткое описание книги')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text='Выберите жанр для этой книги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    """Модель представляет автора"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'