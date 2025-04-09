from django.contrib import admin
from .models import (
    Actor, Genre, Play, TheatreHall,
    Performance, Reservation, Ticket
)

# Set Inline
class ActorInline(admin.TabularInline):
    model = Play.actors.through
    extra = 1


class GenreInline(admin.TabularInline):
    model = Play.genres.through
    extra = 1

# Register PlayAdmin
class PlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = [ActorInline, GenreInline]
    exclude = ('actors', 'genres')

# Register other models
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(TheatreHall)
admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Ticket)
