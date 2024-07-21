from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())
    parent_category_name = serializers.CharField(source='parent_category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    unit_of_sale_name = serializers.CharField(source='unit_of_sale.unit_name', read_only=True)
    delivery_option_name = serializers.CharField(source='delivery_option.option_name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('is_active',)
