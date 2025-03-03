from django.contrib import admin
from .models import Team
from django import forms


class TeamAdminForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'rating', 'strength', 'members']


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = ('name', 'rating', 'strength')
    search_fields = ('name',)


admin.site.register(Team, TeamAdmin)
