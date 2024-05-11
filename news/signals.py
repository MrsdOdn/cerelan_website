from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import News
from news_image.models import NewsImage


@receiver(post_save, sender=News)
def create_news_image(sender, instance, created, **kwargs):
    if created and instance.image:  # Eğer haber oluşturuldu ve bir resim yüklendi ise
        NewsImage.objects.create(news=instance,
                                 file_path=instance.image.url)  # NewsImage modeline resmin dosya yolunu ekler
