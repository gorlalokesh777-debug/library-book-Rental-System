from rest_framework import serializers
from .models import BookRental


class BookRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRental
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
