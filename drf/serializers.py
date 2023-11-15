from rest_framework import serializers
from drf import models


class ProposeModelSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.ProposeModel
        fields = '__all__'


class NewsModelSerializerMany(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = models.News
        fields = ["title", "category", "timestamp"]


class NewsModelSerializerOne(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = models.News
        fields = ["title", "description", "category", "timestamp"]
