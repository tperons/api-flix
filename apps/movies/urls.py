from django.urls import path

from apps.movies.views import (
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
    MovieStatsView,
)

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie_detail'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie_stats')
]
