from django.db import models

from ceralan_website.core.base_model import BaseModel


# Create your models here.
class Service(BaseModel):
    city = models.CharField(unique=True, max_length=30,
                            blank=False, null=False)

    def __str__(self):
        return f"{self.city}"

    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created_at']
