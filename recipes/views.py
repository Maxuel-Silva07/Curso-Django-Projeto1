from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', status=200)

def contato(request):
    return render(request, 'temp/temp.html')

def sobre(request):
    return HttpResponse('S O B R E')

