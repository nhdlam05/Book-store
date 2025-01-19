# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
    
    # Custom validation cho title và author nếu cần
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def validate_author(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Author name must be at least 3 characters long.")
        return value
