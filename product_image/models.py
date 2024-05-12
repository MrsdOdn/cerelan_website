from django.db import models
from ceralan_website.core.base_model import BaseModel


class ProductImage(BaseModel):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='product_images')
    file_path = models.CharField(max_length=255,
                                 null=True, blank=True)  # Resmin dosya yolunu tutmak için karakter alanı

    def __str__(self):
        return f"Image for {self.product.id}. product"

    class Meta:
        db_table = 'product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Products Images'
        ordering = ['-created_at']
