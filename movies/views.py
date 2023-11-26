from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    render(request, 'movies/index.html', {'movies', movies})



def detail(request , movie_id):

    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie/detail.html', {'movie', movie})