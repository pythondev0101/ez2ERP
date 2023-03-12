from django.shortcuts import render



def timeline(request):
    return render(request, 'social/wall.html', context={})


def profile(request):
    return render(request, 'social/profile.html', context={})