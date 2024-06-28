from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from accounts.services import sign_up_user, account_edit, user_edit
from accounts.forms import ProfileCompanyForm, ProfileUserForm
from accounts.utils import AccountTemplates


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

        user = authenticate(request, username=username, password=password)
        if user is None:
            error(request, "Login failed, please try again")
            return redirect('login')

        login(request, user)
        return redirect('dashboard')


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
        business_name = request.POST['business_name']

        try:
            sign_up_user(
                fname=fname, 
                lname=lname,
                username=username,
                password=password,
                business_name=business_name
            )            
            success(request, 'Account created successfully!')
            return redirect('login')
        except IntegrityError:
            error(request, 'Username already exists')
            return redirect('signup')


@login_required
def profile_profile(request):
    if request.method == "POST":
        update_what = request.POST['update_what']
        if update_what == "COMPANY":
            profile_company_form = ProfileCompanyForm(request.POST)
            profile_user_form = ProfileUserForm()

            if profile_company_form.is_valid():
                account_edit(
                    account_id=request.user.profile.account.id,
                    name=profile_company_form.cleaned_data['name']
                )
                success(request, 'Company updated successfully!')
                return redirect('accounts:profile')
        elif update_what == "USER":
            profile_company_form = ProfileCompanyForm()
            profile_user_form = ProfileUserForm(request.POST)

            if profile_user_form.is_valid():
                user_edit(
                    user_id=request.user.id,
                    first_name=profile_user_form.cleaned_data['first_name'],
                    last_name=profile_user_form.cleaned_data['last_name'],
                    email=profile_user_form.cleaned_data['email'],
                    username=profile_user_form.cleaned_data['username']
                )
                success(request, 'User updated successfully!')
                return redirect('accounts:profile')
    else:
        profile_company_form = ProfileCompanyForm()
        profile_user_form = ProfileUserForm()

    user = request.user
    context={
        "user": user,
        "breadcrumb":{"parent":"Profile","child":"Profile Edit"},
        "profile_company_form": profile_company_form,
        "profile_user_form": profile_user_form
    }
    print(profile_company_form.errors)
    return render(request, 'accounts/profile/profile.html', context=context)


# @require_http_methods(["POST"])
# @login_required
# def profile_user_edit(request):
#     pass


# @require_http_methods(["POST"])
# @login_required
# def profile_company_edit(request):

    