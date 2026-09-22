from django import forms
from .models import BookRental


class BookRentalForm(forms.ModelForm):
    class Meta:
        model = BookRental
        fields = [
            'book_title',
            'author_name',
            'borrower_name',
            'borrower_email',
            'rental_date',
            'return_date',
            'status',
            'fine_amount',
        ]
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'borrower_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter borrower name'}),
            'borrower_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'borrower@example.com'}),
            'rental_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'fine_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
