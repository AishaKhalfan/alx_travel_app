"""
Serializers for the listings app
"""
from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Listing
        fields = '__all__'
