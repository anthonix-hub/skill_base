from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import product_details,comment

class signupForm(UserCreationForm):
    first_name = forms.CharField(max_length =20,required =True )
    last_name = forms.CharField(max_length =20,required =True )
    email = forms.EmailField(max_length =30,required =True )

# class postAdmin(admin):
#     form = postAdmin

    class mata:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

# class postAdminFormForm(forms.ModelForm):
#     content = forms.CharField( widget=CKEditorWidget(
    #        attrs={
    #     'class':'form-control',
    #     'placholder':"type your comment",
    #     'rows':'4',
    # }   
    #  ))

    # class Meta:
    #     model = product_details

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name','email','content')