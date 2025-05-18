"""
URL patterns for the listings app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'listings'

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'listings', views.ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
