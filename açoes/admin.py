from django.contrib import admin
from .models import Actions

@admin.register(Actions)


class ActionsAdmin(admin.ModelAdmin):
    list_display = (
        'name_action', 'institution_organizing', 'city',
        'neighborhood', 'address', 'description'
    )

    search_fields = ('name_action', 'institution_organizing')