from django.db import models
from ceralan_website.core.base_model import BaseModel


class ProductCategory(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='subcategories', null=True, blank=True)
    name = models.CharField(unique=True, max_length=30, blank=False, null=False)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} - {self.name}"
        return self.name

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ['name']
