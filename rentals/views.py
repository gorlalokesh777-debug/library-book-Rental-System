from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import BookRental
from .forms import BookRentalForm


# ----------------------------
# Function-Based Views (FBVs)
# ----------------------------

def home(request):
    """Home page showing a quick summary of rentals."""
    total_rentals = BookRental.objects.count()
    borrowed_count = BookRental.objects.filter(status='Borrowed').count()
    overdue_count = BookRental.objects.filter(status='Overdue').count()
    returned_count = BookRental.objects.filter(status='Returned').count()

    context = {
        'total_rentals': total_rentals,
        'borrowed_count': borrowed_count,
        'overdue_count': overdue_count,
        'returned_count': returned_count,
    }
    return render(request, 'rentals/home.html', context)


def rental_list(request):
    """List all book rental records."""
    rentals = BookRental.objects.all()
    return render(request, 'rentals/rental_list.html', {'rentals': rentals})


def rental_detail(request, pk):
    """Show full details of a single book rental record."""
    rental = get_object_or_404(BookRental, pk=pk)
    return render(request, 'rentals/rental_detail.html', {'rental': rental})


# ----------------------------
# Class-Based Views (CBVs)
# ----------------------------

class RentalCreateView(CreateView):
    """Add a new book rental record."""
    model = BookRental
    form_class = BookRentalForm
    template_name = 'rentals/rental_form.html'
    success_url = reverse_lazy('rental_list')

    def form_valid(self, form):
        messages.success(self.request, 'Book rental record added successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add New Book Rental'
        return context


class RentalUpdateView(UpdateView):
    """Update an existing book rental record."""
    model = BookRental
    form_class = BookRentalForm
    template_name = 'rentals/rental_form.html'
    success_url = reverse_lazy('rental_list')

    def form_valid(self, form):
        messages.success(self.request, 'Book rental record updated successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Book Rental'
        return context


class RentalDeleteView(DeleteView):
    """Delete a book rental record with a confirmation page."""
    model = BookRental
    template_name = 'rentals/rental_confirm_delete.html'
    success_url = reverse_lazy('rental_list')

    def form_valid(self, form):
        messages.success(self.request, 'Book rental record deleted successfully.')
        return super().form_valid(form)
