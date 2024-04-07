from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    img = models.URLField(max_length=500)
    content = models.CharField(max_length=1000)
    date = models.DateField()