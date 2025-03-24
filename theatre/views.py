from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Performance, Ticket
from rest_framework import viewsets, permissions
from django.utils.timezone import now
from django.contrib.auth.models import User


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


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    filter_backends = [filters.SearchFilter]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description'] # ?search=taey


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['show_time']    # ?show_time=2025-03-21

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
    queryset = Reservation.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # if swagger_fake_view is True, return empty queryset
        if getattr(self, 'swagger_fake_view', False):
            return Reservation.objects.none()
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

# ---
class PerformanceSeatsView(APIView):
    def get(self, request, pk):
        try:
            performance = Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            return Response({'error': 'Performance not found'}, status=status.HTTP_404_NOT_FOUND)
        
        hall = performance.theatre_hall
        total_rows = hall.rows
        seats_in_row = hall.seats_in_row

        # reserved seats : {(row, seat), True}
        reserved = set(Ticket.objects.filter(performance=performance).values_list('row', 'seat'))

        seat_map = []
        for row in range(1, total_rows + 1):
            seat_row = []
            for seat in range(1, seats_in_row + 1):
                seat_row.append({
                    'row': row,
                    'seat': seat,
                    'reserved': (row,seat) in reserved
                })
            seat_map.append(seat_row)

        return Response({
            'performance_id': performance.id,
            'hall': hall.name,
            'seat_map': seat_map
        })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]