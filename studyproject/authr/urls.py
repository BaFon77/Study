from django.urls import path, include
from . import views
from .views import Register, LoginUser, PasswordResetUser, PasswordChangeUser
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index),
    #path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('password_reset/', PasswordResetUser.as_view(), name='password_reset'),
    path("password_change/", PasswordChangeUser.as_view(), name="password_change"),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]