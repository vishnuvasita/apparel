from django.urls import path
from .views import Home, about, contact

app_name = 'Home'

urlpatterns = [
    path('', Home, name='Home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]