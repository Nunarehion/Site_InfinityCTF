from django.shortcuts import render
from django.contrib.auth.models import User


def rating(request):
    users = User.objects.filter(
        is_staff=False).order_by('-userprofile__rating')
    return render(request, 'rating.html', {'users': users})
