from django.db import models
from ceralan_website.core.base_model import BaseModel
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Product(BaseModel):
    account = models.ForeignKey('account.MyUser', on_delete=models.CASCADE, related_name='products', blank=False,
                                null=False)
    parent_category = models.ForeignKey('product_category.ProductCategory', on_delete=models.CASCADE,
                                        related_name='parent_products', blank=False, null=False)
    subcategory = models.ForeignKey('product_category.ProductCategory', on_delete=models.CASCADE,
                                    related_name='sub_products', blank=False, null=False)
    unit_of_sale = models.ForeignKey('unit_of_sale.UnitOfSale', on_delete=models.CASCADE, related_name='products')
    delivery_option = models.ForeignKey('delivery_option.DeliveryOption', on_delete=models.CASCADE,
                                        related_name='products', blank=False, null=False)
    seller_first_name = models.CharField(max_length=64, blank=False, null=False)
    seller_last_name = models.CharField(max_length=64, blank=False, null=False)
    seller_contact_no = models.CharField(max_length=10, null=False, blank=False)

    image = models.ImageField(
        upload_to='product_images/{parent_category}/{subcategory}',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
        ],
        help_text=_('Lütfen JPG, JPEG veya PNG formatında bir resim yükleyin.')
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.parent_category} - {self.subcategory}"

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
