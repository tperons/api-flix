from django.contrib import admin

from apps.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('actors',)
    list_display = ('title', 'release_year', 'genre',)
    list_filter = ('genre', 'release_year',)
    search_fields = ('title', 'summary',)
