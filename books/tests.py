from django.test import TestCase
from django.urls import reverse

from books.models import Book
from books.models import Book

# Create your tests here.


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response,"No books found.")

    def test_books_list(self):
        Book.objects.create(title='Book1',description='Book1 description',isbn='12345')
        Book.objects.create(title='Book2',description='Book2 description',isbn='142345')
        Book.objects.create(title='Book3',description='Book3 description',isbn='127345')

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response,book.title)
    def test_books_detail(self):
        book = Book.objects.create(title='Book1',description='Book1 description',isbn='12345')
        response = self.client.get(reverse('books:detail',kwargs={'id': book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
