from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer
    user = UserSerializer

    class Meta:
        model = BookReview
        fields = '__all__'