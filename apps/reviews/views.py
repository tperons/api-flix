from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticated,
)

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer


class ReviewView:
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListCreateView(ReviewView, ListCreateAPIView):
    pass


class ReviewRetrieveUpdateDestroyView(ReviewView, RetrieveUpdateDestroyAPIView):
    pass
