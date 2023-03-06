from django.db import models


# Create your models here.
class Greeting(models.Model):
    greetings_text = models.CharField(max_length=10)
