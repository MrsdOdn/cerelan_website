from rest_framework import serializers

from minibus.models import Minibus


class MinibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minibus
        fields = '__all__'
