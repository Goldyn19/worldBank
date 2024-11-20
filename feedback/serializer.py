from rest_framework import serializers
from .models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'

    def validate_email(self, value):
        if FeedBack.objects.filter(email=value).exists():
            raise serializers.ValidationError("A feedback entry with this email already exists.")
        return value
