from rest_framework import serializers
from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at']
        extra_kwargs = {
            'sensor_id': {
                'write_only': True
            }
        }


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

