from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Register

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' ,'email','password1','password2']

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['occupation','address','gender','phone','religion','marital_status','nid']
        widgets = {
            'gender': forms.RadioSelect(),
            'marital_status': forms.RadioSelect()
        }

class UserUpdateForm(forms.ModelForm):
   email = forms.EmailField()

   class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

class UserRegistrationUpdateForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['occupation','address','gender','phone','religion','marital_status','nid']
        widgets = {
            'gender': forms.RadioSelect(),
            'marital_status': forms.RadioSelect()
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
