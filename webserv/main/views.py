from django.shortcuts import render


def index(request):
    msg = request.GET['message']
    name = request.GET['name']
    return render(request, 'main/index.html', {'message': msg, 'name': name})

def short(request):
    return render(request, 'main/short.html')