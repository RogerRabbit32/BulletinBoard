from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from random import randint

from .models import Code
from .forms import SignUpForm, ConfirmationForm


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.is_active = False
        user.save()
        number = randint(100, 999)
        Code.objects.create(number=number, user=user)
        send_mail(
            subject='Registration confirmation',
            message=f'Ваш код подтверждения регистрации: {number}',
            from_email='levinkirill@yandex.ru',
            recipient_list=[f'{user.email}']
        )
        return redirect('confirm')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def awaiting_confirmation(request):
    return render(request, 'please_confirm.html')


def account_confirmation(request):
    form = ConfirmationForm(request.POST)
    if form.is_valid():
        #username = form.cleaned_data.get('username')
        #password = form.cleaned_data.get('password1')
        #user = authenticate(username=username, password=password)
        code = form.cleaned_data['code']
        code_obj = Code.objects.get(number=code)
        if code_obj:
            user = code_obj.user
            user.is_active = True
            user.save()
            login(request, user)
    return render(request, 'account_confirmation.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
