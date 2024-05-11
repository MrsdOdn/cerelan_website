from django.db import models

from ceralan_website.core.base_model import BaseModel


# Create your models here.
class NewsCategory(BaseModel):
    # blank:False veritabanında boş olamayacağını belirtir
    name = models.CharField(unique=True, max_length=30,
                            blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'news_category'
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'
        ordering = ['-created_at']
