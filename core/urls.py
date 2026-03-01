from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from auth.views import home_view, SignUpView, verify_email
from auth.forms import LoginForm, SignUpForm


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('auth/login/', LoginView.as_view(template_name='login.html', form_class=LoginForm), name='login'),
    path('auth/logout/', LogoutView.as_view(next_page='/auth/login/'), name='logout'),    
    path('auth/signup/', SignUpView.as_view(template_name='signup.html', form_class=SignUpForm), name='signup'),
    path('auth/verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('captcha/', include('captcha.urls')),

]
