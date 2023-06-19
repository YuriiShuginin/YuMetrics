from rest_framework import serializers
from .models import *


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric
        fields = "__all__"


class MistakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mistake
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    mistakes = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = User
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = "__all__"


class MistakeCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    metric_id = serializers.IntegerField()

    def create(self, validated_data):
        favourite = Mistake(**validated_data)
        favourite.save()
        return Mistake(**validated_data)


class ResultCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    score = serializers.IntegerField()

    def create(self, validated_data):
        result = Result(**validated_data)
        result.save()
        return Result(**validated_data)
