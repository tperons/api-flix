from django.db.models import Avg
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from apps.actors.serializers import ActorSerializer
from apps.genres.serializers import GenreSerializer
from apps.movies.models import Movie


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_year(self, value):
        if value < 1900:
            raise ValidationError(_('A data de lançamento não pode ser inferior a 1900.'))
        elif value > timezone.now().year:
            raise ValidationError(_('O ano de lançamento não pode ser no futuro!'))
        return value

    def validate_summary(self, value):
        if len(value) > 512:
            raise ValidationError(_('O resumo não dve conter mais de 512 caracteres'))


class MovieGetSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'actors', 'release_year', 'rate', 'summary')

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
