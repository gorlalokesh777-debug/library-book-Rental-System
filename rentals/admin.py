from django.contrib import admin
from .models import BookRental


@admin.register(BookRental)
class BookRentalAdmin(admin.ModelAdmin):
    list_display = (
        'book_title', 'author_name', 'borrower_name',
        'rental_date', 'return_date', 'status', 'fine_amount',
    )
    list_filter = ('status',)
    search_fields = ('book_title', 'borrower_name', 'author_name')
