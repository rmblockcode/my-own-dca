from django.contrib import admin
from .models import DCAParameter

@admin.register(DCAParameter)
class DCAParameterAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'exchange_description')
    search_fields = ('exchange_id', 'exchange_description')
