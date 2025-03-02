from users.models import UserProfile
from .forms import SignUpForm
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def logout_view(request):
    logout(request)
    return redirect('/')


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        if form.cleaned_data['avatar']:
            UserProfile.objects.create(
                user=user, avatar=form.cleaned_data['avatar'])
        return super().form_valid(form)
