from django.contrib import admin
from apps.pages.models import Vegatebles, Feedback
# Register your models here.
@admin.register(Vegatebles)
class VegateblesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_ad")
    list_display_links = ("id", "name")

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "email","is_valid", "created_ad")
    list_display_links = ("id", "name")
