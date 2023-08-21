from django.contrib import admin

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('all-books/', all_books),
    path('foreing-books/', foreing_books),
    path('main-page/', main_page),
    path('books-for-school/', books_for_school),
    path('profile/', profile),
    path('search/', search),  # маршрут для функции search в views.py
    path('create/', create_book),  # маршрут для функции create_book в views.py
]