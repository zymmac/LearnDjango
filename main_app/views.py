from django.shortcuts import render
from main_app.models import Shiba

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def shiba(request):

    shiba = Shiba.objects.order_by('name')
    shiba_dict = {'shibas_list': shiba}

    return render(request, 'main_app/shiba.html',context=shiba_dict)
