from django.urls import path, include
from . import views


urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
