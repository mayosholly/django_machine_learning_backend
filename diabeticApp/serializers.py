from rest_framework import serializers
from .models import DiabetesData

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesData
        fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction','Age',]
     