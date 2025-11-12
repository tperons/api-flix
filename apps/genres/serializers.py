from rest_framework.serializers import ModelSerializer

from apps.genres.models import Genre


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)
