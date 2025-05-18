"""
Models for the listings app
"""
from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    """
    Model representing a travel listing
    """
    LISTING_TYPES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
        ('resort', 'Resort'),
        ('villa', 'Villa'),
        ('cabin', 'Cabin'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPES)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    max_guests = models.PositiveIntegerField(default=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
