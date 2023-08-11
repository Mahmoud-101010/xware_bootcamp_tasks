from django import forms
from .models import * 



class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=4)


class SignupForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    first_name = forms.CharField(required=True, min_length=4)
    last_name = forms.CharField(required=True, min_length=6)
    email = forms.EmailField(required=True, min_length=12)
    phone_number=forms.CharField(required=True, min_length=11)
    password = forms.CharField(required=True, min_length=4)

class uploadBlog(forms.Form):
    title=forms.CharField(required=True,min_length=1)
    blog=forms.CharField(required=True,min_length=2)

class updateBlog(forms.Form):
    title=forms.CharField(required=False,min_length=1)
    blog=forms.CharField(required=False,min_length=2)
    post_img=forms.ImageField(required=False)

