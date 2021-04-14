from django.shortcuts import render, redirect

# Imports to get and set Auth Forms and login.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

"""
Static methods to set SingUp, LogIn and LogOut sessions and
 register in DB.
"""


class AuthMethods:
    @staticmethod
    def signup_view(request):
        """
        Create register and redirect page to /menu/ if form is valid, or
        redirect page to register.
        """

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # log the user
                login(request, user)
                return redirect("/menu/")
        else:
            form = UserCreationForm()
        return render(request, "auth/signup.html", {"form": form})

    @staticmethod
    def login_view(request):
        """
        Log in user and redirect page to /menu/ if form is valid, or
        redirect page to Login if the session is not logged in.
        """

        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # log in the user
                user = form.get_user()
                login(request, user)
                return redirect("/menu/")
        else:
            form = AuthenticationForm()
        return render(request, "auth/login.html", {"form": form})

    @staticmethod
    def logout_view(request):
        """
        Log out user and redirect page to /login/ path.
        """

        if request.method == "POST":
            logout(request)
            return redirect("/login/")
