from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.login_page, name='login-page'),
    path('signup-student', views.signup_student, name='signup-student'),
    path('signin-student', views.signin_student, name='signin-student'),
    path('signup-admin', views.signup_admin, name='signup-admin'),
    path('signin-admin', views.signin_admin, name='signin-admin'),
    path('logout', views.logout_page, name='logout-page')

]