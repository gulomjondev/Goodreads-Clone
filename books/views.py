from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from books.forms import BookReviewForm
from books.models import Book, BookReview


class BookListView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q','')
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 2)

        page_num = request.GET.get('page',1)
        page_object = paginator.get_page(page_num)
        context = {
            'page_object': page_object,
            'search_query': search_query,
        }
        return render(request,'books_templates/book_list.html',context)

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'books_templates/book_detail.html'
#     context_object_name = 'book'
#     pk_url_kwarg = "id"

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, 'books_templates/book_detail.html', context)

class AddReviewView(LoginRequiredMixin,View):
    def post(self,request,id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = request.user,
                stars_given= review_form.cleaned_data['stars_given'],
                comment = review_form.cleaned_data['comment'],
            )
            return redirect(reverse('books:detail',kwargs={'id':book.id}))

        return render(request, 'books_templates/book_detail.html', {'review_f orm': review_form,'book':book})