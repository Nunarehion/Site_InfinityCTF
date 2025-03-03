from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя команды')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    strength = models.IntegerField(
        default=0, verbose_name='Сила')
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


@receiver(m2m_changed, sender=Team.members.through)
def update_user_profiles(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove"]:
        for user in instance.members.all():
            user.userprofile.team = instance if instance.members.filter(
                id=user.id).exists() else None
            user.userprofile.save()
