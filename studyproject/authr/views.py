from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import UserCreationForm, LoginUserForm, UserPasswordResetForm, UserPasswordChangeForm


def index(request):
    return render(request, 'authr/index.html')

# def about(request):
#     return HttpResponse()

def reg(request):
    return render(request, 'registration/register.html')


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            print('Вы успешно зарегистрировались!')
            return redirect('/')
        else:
            form.add_error(None, 'Unknown or disabled account')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'



class PasswordResetUser(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'registration/password_reset_forms.html'



class PasswordChangeUser(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/password_change_forms.html'