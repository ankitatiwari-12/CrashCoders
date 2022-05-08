from django.db import models


class oppo(models.Model):
	long_url=models.URLField(max_length=250)
	short_url=models.CharField(max_length=50,unique=True)
	date=models.DateField(auto_now_add=True)
	clicks=models.IntegerField(default=0)
# Create your models here.
