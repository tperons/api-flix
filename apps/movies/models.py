from django.db import models

from apps.actors.models import Actor
from apps.genres.models import Genre


class Movie(models.Model):

    class Meta:
        ordering = ('-release_year', 'title',)
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    title = models.CharField(verbose_name='Título', max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies', verbose_name='Gênero')
    release_year = models.IntegerField(verbose_name='Ano de Lançamento', blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name='Atores/Atrizes')
    summary = models.TextField(verbose_name='Resumo', blank=True)

    def __str__(self):
        return self.title
