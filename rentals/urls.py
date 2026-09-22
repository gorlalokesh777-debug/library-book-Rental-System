from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rentals/', views.rental_list, name='rental_list'),
    path('rentals/<int:pk>/', views.rental_detail, name='rental_detail'),
    path('rentals/add/', views.RentalCreateView.as_view(), name='rental_add'),
    path('rentals/<int:pk>/edit/', views.RentalUpdateView.as_view(), name='rental_edit'),
    path('rentals/<int:pk>/delete/', views.RentalDeleteView.as_view(), name='rental_delete'),
]
