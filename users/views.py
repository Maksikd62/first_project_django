from django.shortcuts import redirect, render
from django.http import HttpResponse

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User

import os
from django.conf import settings

def list(request):
    users = User.objects.all()
    return render(request, "list_user.html", {"users": users})

def detail(request, id):
    try:
        user = User.objects.get(id=id)
        return render(request, "detail_user.html", {"user": user})
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    
def delete(request, id):
    try:
        user = User.objects.get(id=id)
        if user.avatar:
            os.remove(os.path.join(settings.MEDIA_ROOT, user.avatar.name))
        user.delete()
        return redirect("/users")
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    
def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "create_user.html", {"form": form})


def edit(request, id):

    user = User.objects.get(id=id)

    if user is None:
        return HttpResponse("User not found")

    form = EditUser(instance=user)

    if request.method == "POST":
        form = CreateUser(request.POST, instance=user, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "edit_user.html", {"form": form})