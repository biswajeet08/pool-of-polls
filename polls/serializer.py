from rest_framework import serializers
from .models import Create_Poll

class PollSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=150)
    category = serializers.CharField(max_length=20)
    item1 = serializers.CharField(max_length=100)
    img1 = serializers.ImageField()
    item2 = serializers.CharField(max_length=100)
    img2 = serializers.ImageField()
    item3 = serializers.CharField(max_length=100)
    img3 = serializers.ImageField()
    item4 = serializers.CharField(max_length=100)
    img4 = serializers.ImageField()
    count1 = serializers.IntegerField()
    count2 = serializers.IntegerField()
    count3 = serializers.IntegerField()
    count4 = serializers.IntegerField()
    total = serializers.IntegerField()
    percent1 = serializers.FloatField()
    percent2 = serializers.FloatField()
    percent3 = serializers.FloatField()
    percent4 = serializers.FloatField()

    def create(self, validated_data):
        return Create_Poll.objects.create(**validated_data)