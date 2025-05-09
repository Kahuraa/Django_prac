from django import forms

from myapp.models import Person


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect)
    class Meta:
        model = Person
        fields = ('name', 'height', 'email', 'dob', 'phone', 'weight', 'gender', 'profile_pic')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min': '1990-01-01', 'max': '2009-12-31'}),
            'weight': forms.NumberInput(attrs={'type': 'number', 'min': 20, 'max': 120}),
            'height': forms.NumberInput(attrs={'type': 'number', 'min': 1.4, 'max': 2.5}),
        }


        class loginForm(forms.Form):
            username = forms.CharField(label='Username', max_length=100)
            password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())




# python manage.py createsuperuser
# admin
# Pineappl$s25