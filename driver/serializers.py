from rest_framework import serializers

from driver.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    departure_location_city = serializers.CharField(source='departure_location.city', read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'
