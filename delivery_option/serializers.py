from rest_framework import serializers

from delivery_option.models import DeliveryOption


class DeliveryOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOption
        fields = '__all__'
