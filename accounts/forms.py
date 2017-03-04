from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

"""
Creating the form by specifying its label names and input type. Label names are the variables we give to it.
This classs only makes the form; we have to add <form> tag and <button> by ourselves in HTML.
"""
class RegistrationForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    # label required other wise label shown is Password2
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    def clean_username(self):
        username=self.cleaned_data.get('username')

        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError('Username already taken')

        return username

    def clean_password2(self):
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')

        if password!=password2:
            raise forms.ValidationError('Passwords don\'t match')

        return password

    def clean_email(self):
        email=self.cleaned_data.get('email')

        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError('Email already taken')

        return email