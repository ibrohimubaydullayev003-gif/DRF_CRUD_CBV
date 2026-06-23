from rest_framework import serializers
from .models import Car
from rest_framework.exceptions import ValidationError

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate(self, attrs):
        name = attrs.get('name')
        if name.isdigit():
            raise ValidationError({'error': "name son bo'lmasligi kerak"})
        return attrs

    def validate_price(self, value):
        if value < 0:
            raise ValidationError({'error': "narxni to'g'ri kiriting"})
        return value
        