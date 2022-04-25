from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages




# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-horizontal'}))
#     username = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-horizontal'}))
