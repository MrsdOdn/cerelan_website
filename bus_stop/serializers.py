from rest_framework import serializers

from bus_stop.models import BusStop


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'
