from rest_framework import serializers

from minibus.models import Minibus


class MinibusSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Minibus
        fields = '__all__'
        read_only_fields = ('is_active',)
