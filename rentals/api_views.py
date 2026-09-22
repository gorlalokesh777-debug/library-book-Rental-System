from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import BookRental
from .serializers import BookRentalSerializer


# ----------------------------------------
# 1) ModelViewSet (used with DRF router)
# ----------------------------------------
class BookRentalViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, partial_update, destroy
    automatically. Registered with a router in api_urls.py.
    """
    queryset = BookRental.objects.all()
    serializer_class = BookRentalSerializer


# ----------------------------------------
# 2) Generic Class-Based API Views
# ----------------------------------------
class BookRentalListCreateAPIView(ListCreateAPIView):
    """Handles GET (list) and POST (create)."""
    queryset = BookRental.objects.all()
    serializer_class = BookRentalSerializer


class BookRentalDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Handles GET (retrieve), PUT, PATCH (update), DELETE (destroy)."""
    queryset = BookRental.objects.all()
    serializer_class = BookRentalSerializer
