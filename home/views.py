from django.shortcuts import render, redirect



def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        context = {'title': 'ez2ERP'}
        return render(request, 'home/landing_page.html', context=context)

# def landing_page(request):
#     context = {
#         'title': 'ez2ERP'
#     }
#     return render(request, 'home/landing_page.html', context=context)


def dashboard(request):
    return render(request, 'home/dashboard/dashboard.html', {})