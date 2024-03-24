from django.urls import path
from .views import HelloWorldView
from .views import StockPredictionView


urlpatterns = [
    path('api/helloworld', HelloWorldView.as_view(), name='hello-world'),
    path('api/predict-stock/', StockPredictionView.as_view(), name='predict-stock'),

]