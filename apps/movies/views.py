from django.db.models import Avg, Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from apps.movies.models import Movie
from apps.movies.serializers import MovieGetSerializer, MovieSerializer
from apps.reviews.models import Review


class MovieView:
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)
    queryset = Movie.objects.select_related('genre').prefetch_related('actors', 'reviews')


class MovieListCreateView(MovieView, ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieGetSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(MovieView, RetrieveUpdateDestroyAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieGetSerializer
        return MovieSerializer


class MovieStatsView(MovieView, APIView):

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_star = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_star': round(average_star, 1) if average_star else 0,
            },
            status=HTTP_200_OK,
        )
