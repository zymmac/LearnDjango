from django.urls import path
from main_app import views

# SET THE NAMESPACE!
app_name = 'main_app'

urlpatterns = [
    path('shiba/', views.shiba, name='shiba'),
    path('form/', views.formpage, name='form')
]
