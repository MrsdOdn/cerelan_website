from rest_framework import serializers

from unit_of_sale.models import UnitOfSale


class UnitOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfSale
        fields = '__all__'
