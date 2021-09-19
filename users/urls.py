"""Defines URL patterns for the users."""

from django.urls import path, include

from users import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register')
]
