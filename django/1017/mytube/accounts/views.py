from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = '/tube/',
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
    next_page = '/tube/',
)

logout = LogoutView.as_view(
    next_page = '/tube/',
)

@login_required
def profile(request):
    return render(request, '/accounts/profile.html')