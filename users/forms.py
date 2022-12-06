# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,PasswordChangeForm
from django.contrib.auth.models import User


class RegiterUserCreationForm(UserCreationForm):
    
    class Meta:
        # fields = UserCreationForm.Meta.fields + ("email",)
        model =User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text',     
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email',  
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password',  
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'input is-success is-rounded', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            }) 



class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget = forms.EmailInput(attrs={"class": "input is-success is-rounded"})

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
       
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "input is-success is-rounded"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "input is-success is-rounded"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "input is-success is-rounded"})



        