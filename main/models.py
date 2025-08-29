from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from io import BytesIO
from django.core.files import File
import qrcode

User = get_user_model()


class FoodDonation(models.Model):
    restaurant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    expiry_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    
    # Will be stored in Cloudinary
    photo = models.ImageField(upload_to='food_photos/', blank=True, null=True)

    added_at = models.DateTimeField(auto_now_add=True)
    is_claimed = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, default='0000000000')
    
    delivered = models.BooleanField(default=False)
    # Will be stored in Cloudinary
    delivery_photo = models.ImageField(upload_to='delivery_photos/', blank=True, null=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    # QR code also goes to Cloudinary
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    claimed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='claimed_donations'
    )

    def __str__(self):
        return f"{self.food_name} from {self.restaurant.username}"
    
    def generate_qr_code(self):
        """
        Generate a QR code for verifying pickup.
        This image will also be saved in Cloudinary.
        """
        url = f"http://127.0.0.1:8000/verify-pickup/{self.id}/"  # Replace with your production domain
        qr = qrcode.make(url)
        blob = BytesIO()
        qr.save(blob, format='PNG')
        blob.seek(0)  # ✅ reset the pointer before saving
        self.qr_code.save(f"donation_{self.id}_qr.png", File(blob), save=False)

    def save(self, *args, **kwargs):
        """
        Override save to generate QR code if not already present.
        """
        super().save(*args, **kwargs)  # First save to get an ID
        if not self.qr_code:
            self.generate_qr_code()
            super().save(update_fields=['qr_code'])
