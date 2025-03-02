from django.db import models
from django.contrib.auth.models import User
from teams.models import Team


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='images/users', verbose_name='Изображение', blank=True)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Команда')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
