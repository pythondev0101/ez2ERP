from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
from django.contrib.auth.models import User
from django.db.utils import IntegrityError



def login_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            context = {}
            return render(request, 'accounts/auth/login.html', context=context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        login_redirect = request.POST['loginRedirect']

        user = authenticate(request, username=username, password=password)
        if user is None:
            error(request, "Login failed, please try again")
            return redirect('login')

        if login_redirect == 'loginSocial':
            return redirect('timeline')
        elif login_redirect == 'loginConsole':
            return redirect('dashboard')
        else:
            error(request, "Login failed, please try again")
            return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_user(request):
    if request.method == "GET":
        return render(request, 'accounts/auth/signup.html', context={})
    elif request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create(
                first_name=fname,
                last_name=lname,
                username=username,
            )
            user.set_password(password)
            user.save()
        except IntegrityError:
            error(request, 'Username already exists')
            return redirect('signup')
        else:
            success(request, 'Account created successfully!')
            return redirect('login')
