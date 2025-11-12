from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.movies.models import Movie


class Review(models.Model):

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    class Stars(models.IntegerChoices):
        ONE = 1, _('1')
        TWO = 2, _('2')
        THREE = 3, _('3')
        FOUR = 4, _('4')
        FIVE = 5, _('5')

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', verbose_name='Filme')
    stars = models.IntegerField(verbose_name='Estrelas', choices=Stars)
    comment = models.TextField(verbose_name='Comentário', blank=True)

    def __str__(self):
        return self.movie
