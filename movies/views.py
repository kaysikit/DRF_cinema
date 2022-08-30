from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод фильма"""
    def get(self, request, pk):
        movies = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data)