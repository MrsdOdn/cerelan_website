from django.db import models
from ceralan_website.core.base_model import BaseModel


class DeliveryOption(BaseModel):
    option_name = models.CharField(unique=True, max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.option_name}"

    class Meta:
        db_table = 'delivery_option'
        verbose_name = 'Delivery Option'
        verbose_name_plural = 'Delivery Options'
        ordering = ['-created_at']
