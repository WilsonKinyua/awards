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


# profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=250)
    contact = models.CharField(max_length=250)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username
