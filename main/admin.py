from django.contrib import admin
from django.utils.html import format_html
from .models import FoodDonation


@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = (
        "food_name", 
        "restaurant", 
        "quantity", 
        "expiry_time", 
        "is_claimed", 
        "delivered",
        "added_at",
        "photo_preview",
        "qr_preview",
    )
    list_filter = ("is_claimed", "delivered", "expiry_time", "added_at")
    search_fields = ("food_name", "restaurant__username", "location")

    readonly_fields = ("qr_code", "qr_preview", "photo_preview", "delivery_preview")

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.photo.url)
        return "No Photo"
    photo_preview.short_description = "Food Photo"

    def delivery_preview(self, obj):
        if obj.delivery_photo:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.delivery_photo.url)
        return "No Delivery Photo"
    delivery_preview.short_description = "Delivery Photo"

    def qr_preview(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="80" height="80" />', obj.qr_code.url)
        return "No QR"
    qr_preview.short_description = "QR Code"
