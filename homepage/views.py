from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(
        request=request,
        template_name='homepage/home.html',
        context={
            # "form": UserCreationForm
        }
    )


# @login_required
def blog(request):
    return render(
        request=request,
        template_name="homepage/blog.html"
    )


# @login_required
def profile(request):
    return render(
        request=request,
        template_name='account/profile.html',
        context={}
    )


def signup(request):
    if request.method == "GET":
        return render(
            request=request,
            template_name='signup.html',
            context={
                "form": UserCreationForm
            }
        )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Register user
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"]
                )
                user.save()
                # Creating cookie
                login(
                    request=request,
                    user=user,
                    backend='django.contrib.auth.backends.ModelBackend'
                )
                return redirect("demo")
            except IntegrityError:
                return render(
                    request=request,
                    template_name="signup.html",
                    context={
                        "form": UserCreationForm,
                        "error": "Username already exists"
                    }
                )
        return render(
            request=request,
            template_name="signup.html",
            context={
                "form": UserCreationForm,
                "error": "Password do not match"
            }
        )


# @login_required
def signout(request):
    logout(request=request)
    return redirect(to="home")


def signin(request):
    if request.method == "GET":
        return render(
            request=request,
            template_name='signin.html',
            context={
                "form": AuthenticationForm
            }
        )
    else:
        user = authenticate(
            request=request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is None:
            return render(
                request=request,
                template_name='signin.html',
                context={
                    "form": AuthenticationForm,
                    "error": "Username or passsword is incorrect"
                }
            )
        else:
            login(
                request=request,
                user=user,
            )
            # login(
            #         request=request,
            #         user=user,
            #         backend='django.contrib.auth.backends.ModelBackend'
            #     )
            return redirect(to="demo")
