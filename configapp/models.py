from django.db import models

# Create your models here.

class Sms(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    subject=models.CharField(max_length=100)
    message=models.TimeField()

    def __str__(self):
        return self.name

