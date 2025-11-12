from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticated,
)

from apps.actors.models import Actor
from apps.actors.serializers import ActorSerializer


class ActorView:
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorCreateListView(ActorView, ListCreateAPIView):
    pass


class ActorRetrieveUpdateDestroyView(ActorView, RetrieveUpdateDestroyAPIView):
    pass
