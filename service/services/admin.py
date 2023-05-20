from django.contrib import admin

from services.models import Service, Plan, Subscription


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "full_price")


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("plan_type", "discount_percent")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("client", "service", 'plan')
