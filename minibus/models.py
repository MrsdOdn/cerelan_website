from django.db import models
from ceralan_website.core.base_model import BaseModel
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Minibus(BaseModel):
    account = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='minibus')
    driver_first_name = models.CharField(max_length=64, blank=False, null=False)
    driver_last_name = models.CharField(max_length=64, blank=False, null=False)
    driver_contact_no = models.CharField(max_length=10, null=False, blank=False)
    pickup_location = models.CharField(max_length=64, blank=False, null=False)
    drop_off_location = models.CharField(max_length=64, blank=False, null=False)
    pickup_time = models.DateTimeField(blank=False, null=False)
    image = models.ImageField(
        upload_to='minibus_images/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
        ],
        help_text=_('Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.')
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    route = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.pickup_location} - {self.drop_off_location} - {self.pickup_time}"

    class Meta:
        db_table = 'minibus'
        verbose_name = 'Minibus'
        verbose_name_plural = 'Minibuses'
        ordering = ['-created_at']
