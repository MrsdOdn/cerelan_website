from django.core.exceptions import ValidationError
from django.db import models
from ceralan_website.core.base_model import BaseModel
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


def validate_image_size(image):
    return True
    file_size = image.file.size
    limit_kb = 5120  # 5 MB limit
    if file_size > limit_kb * 1024:
        raise ValidationError("Maksimum dosya boyutu 5MB'dir.")


class SharedCar(BaseModel):
    account = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='shared_cars')
    driver_first_name = models.CharField(max_length=64, blank=False, null=False)
    driver_last_name = models.CharField(max_length=64, blank=False, null=False)
    driver_contact_no = models.CharField(max_length=10, null=False, blank=False)
    pickup_location = models.CharField(max_length=64, blank=False, null=False)
    drop_off_location = models.CharField(max_length=64, blank=False, null=False)
    pickup_time = models.DateTimeField(blank=False, null=False)
    image = models.ImageField(
        upload_to='shared_car_images/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
            validate_image_size,
        ],
        help_text=_('Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.')
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    number_of_passengers = models.PositiveIntegerField(default=0, blank=False, null=False)
    route = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.pickup_location} - {self.drop_off_location} - {self.pickup_time}"

    class Meta:
        db_table = 'shared_car'
        verbose_name = 'Shared Car'
        verbose_name_plural = 'Shared Cars'
        ordering = ['-created_at']
