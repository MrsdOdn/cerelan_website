from rest_framework import serializers

from shared_car.models import SharedCar


class SharedCarSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SharedCar
        fields = '__all__'
        read_only_fields = ('is_active',)
