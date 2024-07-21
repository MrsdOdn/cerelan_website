from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ('is_active',)
