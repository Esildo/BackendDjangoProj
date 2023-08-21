from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .models import Book, Author,Genre
import json
from django.db.models import Q
@require_http_methods(["GET"])
def search(request):
    search_query = request.GET.get('q', '')
    try:
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__name__icontains=search_query))
        data = serializers.serialize('json', books)
        return JsonResponse(data, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'No book matches the search term'}, status=404)
@require_http_methods(["GET"])
def all_books(request):
    try:
        books = Book.objects.all()
        data = serializers.serialize('json', books)
        return JsonResponse(data, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'No books found'}, status=404)

def create_book(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        genres_data = data.get('genres')
        author_name = data.get('author_name')
        author_country = data.get('author_country')
        publication_date = data.get('publication_date')

        author, created = Author.objects.get_or_create(name=author_name, country=author_country)
        book = Book.objects.create(title=title, author=author, publication_date=publication_date)
        for genre_name in genres_data:
            genre, created = Genre.objects.get_or_create(name=genre_name)
            book.genres.add(genre)

        response_data = {
            'id': book.id,
            'title': book.title,
            'genres': list(book.genres.values('name')),
            'author': book.author.name,
            'publication_date': book.publication_date.strftime('%Y-%m-%d')
        }
        return JsonResponse(response_data, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
@require_http_methods(["GET", "POST"])
def foreing_books(request):
    return JsonResponse({"page": "Hello foreing books"})

@require_http_methods(["GET", "POST"])
def main_page(request):
        return JsonResponse({"page": "Hello main page"})

@require_http_methods(["GET", "POST"])
def books_for_school(request):
    return JsonResponse({"page": "Hello for school"})

@require_http_methods(["GET", "POST"])
def profile(request):
    return JsonResponse({"page": "Hello profile"})
