from django.db import models
from ceralan_website.core.base_model import BaseModel
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Driver(BaseModel):
    account = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='drivers')
    departure_location = models.ForeignKey('service.Service', on_delete=models.CASCADE, related_name='drivers')
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    profile_picture = models.ImageField(
        upload_to='driver_profile_pictures/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
        ],
        help_text=_('Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.'),
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.departure_location.city}"

    class Meta:
        db_table = 'driver'
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
        ordering = ['-created_at']
