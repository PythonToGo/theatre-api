from rest_framework import viewsets, permissions
from django.utils.timezone import now
from .models import (
    Actor, Genre, Play, TheatreHall,
    Performance, Reservation, Ticket
)
from .serializers import (
    ActorSerializer, GenreSerializer, PlaySerializer,
    TheatreHallSerializer, PerformanceSerializer,
    ReservationSerializer, ReservationDetailSerializer,
    TicketSerializer, CreateTicketSerializer,
    UserSerializer
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.MOdelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    serializer_class = PerformanceSerializer

    def get_queryset(self):
        queryset = Performance.objects.all()
        date = self.request.query_params.get('date', None)
        if date:
            queryset = queryset.filter(show_time__date=date)
        return queryset


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ReservationDetailSerializer
        return ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateTicketSerializer
        return TicketSerializer

