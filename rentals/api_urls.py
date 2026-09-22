from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import (
    BookRentalViewSet,
    BookRentalListCreateAPIView,
    BookRentalDetailAPIView,
)

# --- DRF Router for ModelViewSet ---
# This automatically generates:
# GET/POST   /api/book-rentals/
# GET/PUT/PATCH/DELETE /api/book-rentals/<id>/
router = DefaultRouter()
router.register(r'book-rentals', BookRentalViewSet, basename='bookrental')

# --- Generic Class-Based API View URLs ---
# Separate endpoints so both implementations can be evaluated independently.
generic_urlpatterns = [
    path('generic/book-rentals/', BookRentalListCreateAPIView.as_view(), name='rental-list-create-api'),
    path('generic/book-rentals/<int:pk>/', BookRentalDetailAPIView.as_view(), name='rental-detail-api'),
]

urlpatterns = [
    path('', include(router.urls)),
] + generic_urlpatterns
