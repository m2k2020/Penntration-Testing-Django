from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect("adminpage")
            elif user is not None and user.is_user:
                login(request, user)
                return redirect("cashier")
            else:
                msg = "invalid credentials"
        else:
            msg = "error validating form"
    return render(request, "login.html", {"form": form, "msg": msg})