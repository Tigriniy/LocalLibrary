from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Количество посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'catalog/index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_visits': num_visits,
        }
    )

class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'catalog/book_list.html'