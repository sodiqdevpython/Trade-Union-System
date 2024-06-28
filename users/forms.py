from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserExtraData

class UserSignUpForm(UserCreationForm):
    # full_name = forms.CharField(max_length=256, required=True)
    id_card = forms.CharField(max_length=9, required=True)
    phone_number = forms.CharField(max_length=13, required=True)

    class Meta:
        model = User
        fields = ('id_card', 'phone_number', 'password1', 'password2')
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id_card', 'password')

class UserExtraDataForm(forms.ModelForm):
    class Meta:
        model = UserExtraData
        fields = ('name', 'last_name', 'father_name', 'phone_number', 'under_age_children_number', 'adress', 'born_in', 'employment_at', 'salary', 'job',)
    
class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserExtraData
        fields = ('name', 'last_name', 'father_name', 'phone_number', 'under_age_children_number', 'adress', 'born_in', 'salary',)