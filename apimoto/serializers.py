from apimoto.models import DataBikes
from rest_framework import serializers


class DataBikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBikes
        fields = '__all__'