# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorListSerializer


# создание нового датчика и получение списка всех датчиков с краткой информацией
class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


# добавление измерения
class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# получить информацию по конкретному датчику и изменить датчик
class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

