import datetime
import uuid
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from django.urls import register_converter
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookInputSerializer, BookOutputSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def book_create(request):
    serializer = BookInputSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def get_detail(request, id):
    book = get_object_or_404(Book, id=id)
    serializer = BookOutputSerializer(book)
    return JsonResponse(serializer.data)

@api_view(['PATCH'])
def updateBook(self, request, *args, **kwargs):
    print(kwargs.get('id'))
    book = Book.objects.get(id=kwargs.get('id'))
    if not book:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookInputSerializer(book, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_books(request):
    author_id = request.query_params.get('author_id', None)
    if author_id:
        books = Book.objects.filter(author_id=author_id)
    else:
        books = Book.objects.all()

    published_date = request.query_params.get('published_date', None)
    if published_date:
        try:
            published_date = datetime.strptime(published_date, '%Y-%m-%d')
            books = books.filter(published_date__gte=published_date)
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    title = request.query_params.get('title', None)
    if title:
        books = books.filter(title__icontains=title)

    price = request.query_params.get('price', None)
    if price:
        try:
            price = float(price)
            books = books.filter(price__gte=price)
        except ValueError:
            return Response({"error": "Invalid price format."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = BookOutputSerializer(books, many=True)
    return Response(serializer.data)

