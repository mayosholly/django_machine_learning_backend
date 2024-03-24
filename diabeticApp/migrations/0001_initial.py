# Generated by Django 4.2.3 on 2024-01-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.FloatField()),
                ('Glucose', models.FloatField()),
                ('BloodPressure', models.FloatField()),
                ('SkinThickness', models.FloatField()),
                ('Insulin', models.FloatField()),
                ('BMI', models.FloatField()),
                ('DiabetesPedigreeFunction', models.FloatField()),
                ('Age', models.FloatField()),
            ],
        ),
    ]