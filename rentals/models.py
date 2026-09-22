from django.db import models


class BookRental(models.Model):

    STATUS_CHOICES = [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
        ('Overdue', 'Overdue'),
        ('Lost', 'Lost'),
    ]

    book_title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=150)
    borrower_name = models.CharField(max_length=150)
    borrower_email = models.EmailField()
    rental_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Borrowed')
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.book_title} - {self.borrower_name}"
