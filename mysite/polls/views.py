from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi there! My name is Ali!")
