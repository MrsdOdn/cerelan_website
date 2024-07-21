from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from product_image.models import ProductImage


@receiver(post_save, sender=Product)
def create_product_image(sender, instance, created, **kwargs):
    if created and instance.image:
        ProductImage.objects.create(product=instance,
                                 file_path=instance.image.url)  # Resmin dosya yolunu ekler
