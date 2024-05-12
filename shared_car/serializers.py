from rest_framework import serializers

from shared_car.models import SharedCar


class SharedCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedCar
        fields = '__all__'
