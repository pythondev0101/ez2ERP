"""ez2erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import dashboard, index
from accounts.views import login_user, logout_user, signup_user


urlpatterns = [
    path('', index, name='root'),
    path('home/', index, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('adminsite/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('social/', include('social.urls')),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup')
]
