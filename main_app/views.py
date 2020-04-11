from django.shortcuts import render
from main_app.models import Shiba
from main_app.forms import Shiba_form

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def shiba(request):

    shiba = Shiba.objects.order_by('name')
    shiba_dict = {'shibas_list': shiba}

    return render(request, 'main_app/shiba.html',context=shiba_dict)

def formpage(request):

    if request.method == 'POST':
        form = Shiba_form(request.POST)

        if form.is_valid():
            print('Form successful!')
            print('Shiba name is: '+form.cleaned_data['name'])
            print('Shiba birthday is: '+str(form.cleaned_data['birthday']))
            print('Shiba color is: '+form.cleaned_data['color'])

    else:
        form = Shiba_form()

    return render(request, 'main_app/formpage.html', context={'forms':form})
