from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SharedCar
from car_image.models import CarImage


@receiver(post_save, sender=SharedCar)
def create_car_image(sender, instance, created, **kwargs):
    if created and instance.image:
        CarImage.objects.create(shared_car=instance,
                                 file_path=instance.image.url)  # Resmin dosya yolunu ekler
