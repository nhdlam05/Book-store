"""
URL configuration for book_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import uuid
from django.contrib import admin
from django.urls import path

from apps.book_store_app.views import book_create, get_detail, get_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-book/', book_create, name='create-book'),
    path('get-book/<uuid:id>/', get_detail, name='get-book'),
    path('get-books/', get_books, name='get-book'),
    path('update_book/<uuid:id>/', book_create, name='update-book'),
]