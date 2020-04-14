from django.forms import ModelForm
from main_app.models import Shiba

class ShibaForm(ModelForm):
    class Meta:
        model = Shiba
        fields = '__all__'


    # colors = (
    # ("Black and Tan", "Black and Tan"),
    # ("Red", "Red"),
    # ("Cream", "Cream"),
    # ("Sesame", "Sesame"),
    # )
    #
    # name = forms.CharField(label='Shiba Name')
    # birthday = forms.DateField(label='Shiba Birthday')
    # color = forms.ChoiceField(choices = colors, label = 'Shiba Color')
