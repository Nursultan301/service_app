from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "company_name", "full_address")
