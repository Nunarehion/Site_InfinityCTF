from django.urls import path, include
from . import views


urlpatterns = [
    path('rating/', views.rating, name='rating'),
]
