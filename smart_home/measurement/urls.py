from django.urls import path
from .views import *

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>', SensorDetailView.as_view()),
]
