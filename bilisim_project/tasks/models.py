from django.db import models

class Task(models.Model):
    # id otomatik verileceği için burda modeli tanımlanmadı
    title = models.CharField(max_length=50)
    problem = models.CharField(max_length=100)
    point = models.FloatField()
    level = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    input = models.CharField(max_length=100, blank=True)
    expected_output = models.CharField(max_length=100)