from django.urls import path
from .views import Home, about, contact, profile

app_name = 'Home'

urlpatterns = [
    path('', Home, name='Home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile' )
]