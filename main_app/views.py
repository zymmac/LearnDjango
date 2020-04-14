from django.shortcuts import render
from main_app.models import Shiba
from main_app.forms import ShibaForm

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def shiba(request):

    shiba = Shiba.objects.order_by('name')
    shiba_dict = {'shibas_list': shiba}

    return render(request, 'main_app/shiba.html',context=shiba_dict)

def formpage(request):

    if request.method == 'POST':
        form = ShibaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return shiba(request)
        else:
            print('ERROR FORM INVALID')

    else:
        form = ShibaForm()

    return render(request, 'main_app/formpage.html', context={'forms':form})
