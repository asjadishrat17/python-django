from django.db import models


class destination(models.Model):
    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    special = models.BooleanField(default=False)
# Create your models here.
