from django.db import models
from ceralan_website.core.base_model import BaseModel
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class News(BaseModel):
    author = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='news')
    news_category = models.ForeignKey('news_category.NewsCategory', on_delete=models.CASCADE,
                                      related_name='news')
    image = models.ImageField(
        upload_to='news_images/{news_category}/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
        ],
        help_text=_('Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.')
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.title} - {self.news_category}"

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
