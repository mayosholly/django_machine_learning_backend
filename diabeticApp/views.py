from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StockDataSerializer
import joblib

class StockPredictionView(APIView):
    def post(self, request):
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            # Assuming you have a trained joblib model named 'model.joblib'
            model = joblib.load('diabeticModel/lrmodel.joblib')

            # Get the input features
            features = [serializer.validated_data[feature] for feature in ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction','Age',]]

            # Make a prediction
            prediction = model.predict([features])

            return Response({"prediction": prediction[0]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)
