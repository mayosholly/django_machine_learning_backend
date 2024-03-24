from django.urls import path
from .views import HelloWorldView
from .views import StockPredictionView


urlpatterns = [
    path('api/predict-diabetics/', StockPredictionView.as_view(), name='predict-diabetics'),
]