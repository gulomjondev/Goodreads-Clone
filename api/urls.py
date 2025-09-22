from django.urls import path

from api.views import BookDetailApiView, BookListApiView

app_name = 'api'

urlpatterns = [

    path('reviews/', BookListApiView.as_view(), name='review-list'),
    path('reviews/<int:id>/', BookDetailApiView.as_view(), name='review_detail'),
]