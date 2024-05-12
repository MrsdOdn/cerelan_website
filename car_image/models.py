from django.db import models
from ceralan_website.core.base_model import BaseModel


class CarImage(BaseModel):
    shared_car = models.ForeignKey('shared_car.SharedCar', on_delete=models.CASCADE, related_name='car_images',
                                   blank=True, null=True)
    minibus = models.ForeignKey('minibus.Minibus', on_delete=models.CASCADE, related_name='car_images', blank=True,
                                null=True)
    file_path = models.CharField(max_length=255,
                                 null=True, blank=True)  # Resmin dosya yolunu tutmak için karakter alanı

    def __str__(self):
        return f"Image for {self.id}"

    class Meta:
        db_table = 'car_image'
        verbose_name = 'Car Image'
        verbose_name_plural = 'Car Images'
        ordering = ['-created_at']
