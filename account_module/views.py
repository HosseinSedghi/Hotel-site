from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View

from account_module.forms import LoginForm
from account_module.models import User


# Create your views here.


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account_module/login.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = User.objects.filter(username__exact=username).first()

            if user:
                if user.check_password(password):
                    login(request, user)
                    return redirect('home-page')
                else:
                    form.add_error('password', 'password is invalid')
            else:
                form.add_error('username', 'user not found')

        return render(request, 'account_module/login.html', {
            'form': form
        })


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home-page')