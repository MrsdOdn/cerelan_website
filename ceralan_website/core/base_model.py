from django.db import models

''' Bu sınıf, yalnızca etkin olan nesneleri döndüren özel bir yöneticidir.
    Bu, genellikle veritabanında mantıksal olarak silinmiş nesneleri dışlamak için kullanılır. '''


class OnlyActiveManager(models.Manager):
    def get_queryset(self):
        return (super(OnlyActiveManager, self).get_queryset()
                .filter(is_active=True))


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='updated at')
    is_active = models.BooleanField(default=True)
    # object, tüm nesneleri döndüren varsayılan yöneticidir.
    objects = models.Manager()
    # active, yalnızca etkin nesneleri döndüren özel bir yöneticidir.
    active = OnlyActiveManager()

    class Meta:
        abstract = True
        default_manager_name = 'active'

    # delet, bir nesneyi mantıksal olarak silmek için kullanılır.
    # Yani is_active alanını False olarak ayarlar ve nesneyi kaydeder.
    def delete(self):
        self.is_active = False
        self.save()
