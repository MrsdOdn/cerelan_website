from django.db import models
from ceralan_website.core.base_model import BaseModel


class UnitOfSale(BaseModel):
    unit_name = models.CharField(unique=True, max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.unit_name}"

    class Meta:
        db_table = 'unit_of_sale'
        verbose_name = 'Unit of Sale'
        verbose_name_plural = 'Units of Sale'
        ordering = ['-created_at']
