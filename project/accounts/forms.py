from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-crontol form-control user',
            'placeholder':'Digite seu email...',
            'id':'email',
            'type':'email',
            'name':'email',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

'''class OtherFieldsForm(forms.ModelForm):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control user',
               'placeholder': 'Digite sua idade...',
               'id': 'age',
               'type': 'age',
               'name': 'age',
    }))
    class Meta:
        model = Profile
        fields = ['age']'''