from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.shiba, name='shiba'),
    path('formpage/', views.formpage, name='shiba form'),
]
