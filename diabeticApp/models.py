from django.db import models

# Create your models here.
from django.db import models

class DiabetesData(models.Model):
    Pregnancies = models.FloatField()
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.FloatField()

    def __str__(self):
        return f"class DiabetesData(models.Model): - {self.Pregnancies}, {self.Glucose}, {self.BloodPressure}, {self.SkinThickness}, {self.Insulin}, {self.BMI}, {self.DiabetesPedigreeFunction}, {self.Age}"
