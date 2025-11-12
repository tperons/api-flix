from django.contrib import admin

from apps.actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nationality',)
    list_filter = ('nationality',)
    search_fields = ('name',)
