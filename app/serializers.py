from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecycleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecycleItem
        fields = '__all__'


class RecycleSerializer(serializers.ModelSerializer):
    # userId = UserSerializer(many=False, read_only=True)
    items = RecycleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Recycle
        fields = '__all__'

    # def to_representation(self, instance):
    #     return instance

    # def create(self, validated_data):
    #     items = validated_data.pop('items')
    #     recycle = Recycle.objects.create(**validated_data)
    #     print(recycle)
    #     for item in items:
    #         RecycleItem.objects.create(recycleId=recycle, **item)
    #     return recycle


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BadReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadReason
        fields = '__all__'
