from django.db import models
from ceralan_website.core.base_model import BaseModel


class NewsImage(BaseModel):
    news = models.ForeignKey('news.News', on_delete=models.CASCADE, related_name='news_image')
    file_path = models.CharField(max_length=255,
                                 null=True, blank=True)  # Resmin dosya yolunu tutmak için karakter alanı

    def __str__(self):
        return f"Image for {self.news.title}"

    class Meta:
        db_table = 'news_image'
        verbose_name = 'News Image'
        verbose_name_plural = 'News Images'
        ordering = ['-created_at']
