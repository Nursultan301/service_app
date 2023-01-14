from django.contrib import admin

from services.models import Service, Subscription, Plan

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)