from django import forms

class Shiba_form(forms.Form):
    colors = (
    ("Black and Tan", "Black and Tan"),
    ("Red", "Red"),
    ("Cream", "Cream"),
    ("Sesame", "Sesame"),
    )

    name = forms.CharField(label='Shiba Name')
    birthday = forms.DateField(label='Shiba Birthday')
    color = forms.ChoiceField(choices = colors, label = 'Shiba Color')
