from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

from users.forms.create import CreateUser
from users.forms.edit import EditUser
from users.models import User

import os
from django.conf import settings

def list(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})

def detail(request, id):
    try:
        user = User.objects.get(id=id)
        return render(request, "users/detail.html", {"user": user})
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)

def delete(request, id):
    try:
        user = User.objects.get(id=id)
        if user.avatar:
            try:
                os.remove(os.path.join(settings.MEDIA_ROOT, user.avatar.name))
            except FileNotFoundError:
                pass
        user.delete()
        return redirect("/users")
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

def create(request):

    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/users")

    return render(request, "users/create.html", {"form": form})

def edit(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)

    old_avatar = user.avatar.path if user.avatar else None

    form = EditUser(instance=user)

    if request.method == "POST":
        form = EditUser(request.POST, instance=user, files=request.FILES)

        if form.is_valid():
            updated_user = form.save(commit=False)

            if 'avatar' in request.FILES and old_avatar:
                try:
                    os.remove(old_avatar)
                except FileNotFoundError:
                    pass

            updated_user.save()
            return redirect("/users")

    return render(request, "users/edit.html", {"form": form})

class CustomLoginView(LoginView):

    def form_valid(self, form):
        return super().form_valid(form)
