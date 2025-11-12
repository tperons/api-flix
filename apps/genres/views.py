from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticated,
)

from apps.genres.models import Genre
from apps.genres.serializers import GenreSerializer


class GenreView:
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreCreateListView(GenreView, ListCreateAPIView):
    pass


class GenreRetrieveUpdateDestroyView(GenreView, RetrieveUpdateDestroyAPIView):
    pass
