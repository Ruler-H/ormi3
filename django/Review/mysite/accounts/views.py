from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.conf import settings


# FBV
# def login(request):
#     '''
#     로그인
#     '''
#     return render(request, 'accounts/login.html')

# def logout(request):
#     '''
#     로그아웃
#     '''
#     return render(request, 'accounts/logout.html')

# def signup(request):
#     '''
#     회원가입
#     '''
#     return render(request, 'accounts/signup.html')

# def profile(request):
#     return render(request, 'accounts/profile.html')

# CBV
# 회원가입
signup = CreateView.as_view(
    form_class = UserCreationForm,
    # 기본  URL을 변경
    template_name = 'account/form.html',
    # 로그인 성공했을 때 이동할 URL
    success_url = settings.LOGIN_URL,
)

# 로그인
login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

# 로그아웃
logout = LogoutView.as_view(
    next_page = settings.LOGIN_URL,
)

@login_required
def profile(request):
    '''
    프로필
    '''
    return render(request, 'accounts/profile.html')