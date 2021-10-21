from django.db import models
import datetime as dt

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


# project models
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = CloudinaryField("image")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title



