from django import forms
# from .models import Customer_user
from django.contrib.auth.models import User
from .models import Customer_user
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="confirm_Password")
    phone = forms.CharField(max_length=15)
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email']
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password does not match")
        return clean_data
    
class  UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class  ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer_user
        fields = ['image']
    