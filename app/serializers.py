from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle
        fields = '__all__'


class RecycleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecycleItem
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BadReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadReason
        fields = '__all__'
