from django.db import models


class Actor(models.Model):

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ator/Atriz'
        verbose_name_plural = 'Atores/Atrizes'

    name = models.CharField(verbose_name='Nome', max_length=128)
    birthday = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    nationality = models.CharField(verbose_name='Nacionalidade', max_length=64)

    def __str__(self):
        return self.name
