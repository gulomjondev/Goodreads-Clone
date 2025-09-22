from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookReviewSerializer
from books.models import BookReview


class BookDetailApiView(APIView):
    def get(self, request,id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)
        return Response(serializer.data)

class BookListApiView(APIView):
    def get(self,request):
        book_reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(book_reviews, many=True)
        return Response(serializer.data)