from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.actors.models import Actor


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthday', 'nationality',)

    def validate_birthday(self, value):
        if value < 1900:
            raise ValidationError(_('Tem certeza que esta pessoa ainda está viva?'))
        elif value > timezone.now().year:
            raise ValidationError(_('Esta pessoa veio do futuro?'))
        return value
