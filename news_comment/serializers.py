from rest_framework import serializers

from news_comment.models import NewsComment


class NewsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = '__all__'
