# books/serializers.py
from rest_framework import serializers

from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author_id', 'published_date', 'isbn', 'price']

class BookOutputSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'isbn', 'price', 'author']

    def get_author(self, obj):
        author = obj.author_id
        return AuthorSerializer(author).data