from django.db import models
from ceralan_website.core.base_model import BaseModel


class NewsComment(BaseModel):
    author = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='news_comment')
    news = models.ForeignKey('news.News', on_delete=models.CASCADE, related_name='news_comment')
    content = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return f"{self.author.first_name}-{self.author.last_name}-{self.news.title}"

    class Meta:
        db_table = 'news_comments'
        verbose_name = 'News Comment'
        verbose_name_plural = 'News Comments'
        ordering = ['-created_at']
