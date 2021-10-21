from django.db import models
import datetime as dt

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


# project models
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = CloudinaryField("image")
    url = models.URLField(blank=True)

    def save_project(self):
        self.save()

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


# DesignRate models
class DesignRate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def save_design_rate(self):
        self.save()

    def delete_design_rate(self):
        self.delete()

    @classmethod
    def get_design_rate(cls, id):
        design_rate = DesignRate.objects.filter(project=id).all()
        return design_rate

    def __str__(self):
        return self.project.title


# UsabilityRate models
class UsabilityRate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def save_usability_rate(self):
        self.save()

    def delete_usability_rate(self):
        self.delete()

    @classmethod
    def get_usability_rate(cls, id):
        usability_rate = UsabilityRate.objects.filter(project=id).all()
        return usability_rate

    def __str__(self):
        return self.project.title


# UsabilityRate models
class ContentRate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def save_content_rate(self):
        self.save()

    def delete_content_rate(self):
        self.delete()

    @classmethod
    def get_content_rate(cls, id):
        content_rate = ContentRate.objects.filter(project=id).all()
        return content_rate

    def __str__(self):
        return self.project.title
