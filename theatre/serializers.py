from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Actor, Genre, Play, TheatreHall,
    Performance, Reservation, Ticket
)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PlaySerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = ['id', 'title', 'description', 'actors', 'genres']


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer(read_only=True)
    theatre_hall = TheatreHallSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'row', 'seat', 'performance']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'created_at', 'user']


class ReservationDetailSerializer(serializers.ModelSerializer):
    tickets= TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'created_at', 'user', 'tickets']


class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['row', 'seat', 'performance', 'reservation']

    def validate(self, data):
        # Check if the ticket is already reserved
        if Ticket.objects.filter(
            row=data['row'],
            seat=data['seat'],
            performance=data['performance']
        ).exists():
            raise serializers.ValidationError("This ticket is already reserved")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']