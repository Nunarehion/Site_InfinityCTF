from django.contrib import admin
from .models import Team
from django import forms


class TeamAdminForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', )
    search_fields = ('name',)


admin.site.register(Team, TeamAdmin)
