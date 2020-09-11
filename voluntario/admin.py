from django.contrib import admin
from .models import Voluntary

@admin.register(Voluntary)


class VoluntaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'neighborhood', 'city')
    search_fields = ('name', 'last_name')