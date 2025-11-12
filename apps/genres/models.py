from django.db import models


class Genre(models.Model):

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    name = models.CharField(verbose_name='Nome', max_length=64, unique=True)

    def __str__(self):
        return self.name
