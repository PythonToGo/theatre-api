from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import (
    ActorViewSet, GenreViewSet, PlayViewSet,
    PerformanceViewSet, TheatreHallViewSet,
    ReservationViewSet, TicketViewSet,
    PerformanceSeatsView, UserViewSet
)


# DefaultRouter
router = DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'plays', PlayViewSet)
router.register(r'theatre_halls', TheatreHallViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'users', UserViewSet)

# nested routers
reservation_router = NestedDefaultRouter(router, r'reservations', lookup='reservation')
reservation_router.register(r'tickets', TicketViewSet, basename='reservation-tickets')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reservation_router.urls), name='reservation-tickets'),
    path('performances/<int:pk>/seats/', PerformanceSeatsView.as_view(), name='performance-seats'),
]
