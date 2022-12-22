from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django import forms
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()

class UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': _('Введите логин')}),
        self.fields['email'].widget.attrs.update({'placeholder': _('Введите почту')}),
        self.fields['password1'].widget.attrs.update({'placeholder': _('Введите пароль')}),
        self.fields['password2'].widget.attrs.update({'placeholder': _('Повторите пароль')}),

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        }



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))



class UserPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите почту'}))



class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение нового пароля'}))