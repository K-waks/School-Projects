from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length=50)
    cp = models.CharField(max_length=50)
    trestbps = models.SmallIntegerField()
    chol = models.SmallIntegerField()
    fbs = models.CharField(max_length=50)
    restecg = models.CharField(max_length=50)
    thalach = models.SmallIntegerField()
    exang = models.CharField(max_length=50)
    oldpeak = models.FloatField()
    slope = models.CharField(max_length=50)
    ca = models.CharField(max_length=50)
    thal = models.CharField(max_length=50)
    target = models.CharField(max_length=50)

    def _str__(self):
        return self.first_name
