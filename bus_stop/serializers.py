from rest_framework import serializers

from bus_stop.models import BusStop


class BusStopSerializer(serializers.ModelSerializer):
    service_city = serializers.CharField(source='service.city', read_only=True)

    class Meta:
        model = BusStop
        fields = '__all__'
