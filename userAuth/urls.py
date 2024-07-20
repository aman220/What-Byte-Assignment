from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.land_page, name='land_page'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('change_password/', views.change_password, name='change_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),

    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='reset_form.html'),
         name='password_reset'),
    path('forgot_password/mail_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_complete.html'),
         name='password_reset_complete')
]
