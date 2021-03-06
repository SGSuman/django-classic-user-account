from __future__ import unicode_literals
from django.urls import path, include
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name=settings.THEME_NAME+'/registration/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name=settings.THEME_NAME+'/registration/password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name=settings.THEME_NAME+'/registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
