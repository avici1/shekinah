from django.db import models

# Create your models here.


class Access(models.Model):
    username = models.CharField(max_length=250, null=False)
    lvl = models.CharField(max_length=200, null=False)

