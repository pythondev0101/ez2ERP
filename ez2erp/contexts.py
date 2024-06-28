from django.urls import resolve


def app_name(request):
    print(resolve(request.path))
    return {'app_name': resolve(request.path).app_name}
