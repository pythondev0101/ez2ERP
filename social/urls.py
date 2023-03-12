from django.urls import path
from .views import timeline, profile


urlpatterns = [
    path('timeline', timeline, name='timeline'),
    path('profile', profile, name='profile')
]