from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя команды')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    strength = models.IntegerField(default=0, verbose_name='Сила')
    members = models.ManyToManyField(
        User, related_name='teams', verbose_name='Участники', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.members.exists():
            self.strength = sum(
                member.userprofile.rating for member in self.members.all())
        else:
            self.strength = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
