from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.


def index(request):
    return render(request, "index.html")


@login_required(login_url="/accounts/login/")
def profile(request):  # view profile
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()  # get profile
    project = Project.objects.filter(user_id=current_user.id).all()  # get all projects
    return render(request, "profile.html", {"profile": profile, "images": project})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":

        current_user = request.user

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        bio = request.POST["bio"]
        contact = request.POST["contact"]

        profile_image = request.FILES["profile_pic"]
        profile_image = cloudinary.uploader.upload(profile_image)
        profile_url = profile_image["url"]

        user = User.objects.get(id=current_user.id)

        # check if user exists in profile table and if not create a new profile
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_photo = profile_url
            profile.bio = bio
            profile.contact = contact
            profile.save()
        else:
            profile = Profile(
                user_id=current_user.id,
                profile_photo=profile_url,
                bio=bio,
                contact=contact,
            )
            profile.save_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()

        return redirect("/profile", {"success": "Profile Updated Successfully"})

        # return render(request, 'profile.html', {'success': 'Profile Updated Successfully'})
    else:
        return render(request, "profile.html", {"danger": "Profile Update Failed"})


# save project
@login_required(login_url="/accounts/login/")
def save_project(request):
    if request.method == "POST":

        current_user = request.user

        title = request.POST["title"]
        description = request.POST["description"]
        url = request.POST["url"]
        image = request.FILES["image"]
        # crop image to square
        image = cloudinary.uploader.upload(image, crop="limit", width=500, height=500)
        # image = cloudinary.uploader.upload(image)
        image_url = image["url"]

        project = Project(
            user_id=current_user.id,
            title=title,
            description=description,
            url=url,
            image=image_url,
        )
        project.save_project()

        return redirect("/profile", {"success": "Project Saved Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Project Save Failed"})


# delete project
@login_required(login_url="/accounts/login/")
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete_project()
    return redirect("/profile", {"success": "Project Deleted Successfully"})
