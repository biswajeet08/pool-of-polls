from rest_framework import serializers
from polls.models import Create_Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create_Poll
        fields = '__all__'

    # def create(self, validated_data):
    #     return Create_Poll.objects.create(**validated_data)