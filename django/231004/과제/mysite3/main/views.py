from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def blog(request):
    return render(request, 'blog.html')

def blog_1(request):
    return render(request, 'blog_1.html')

def blog_2(request):
    return render(request, 'blog_2.html')

def blog_3(request):
    return render(request, 'blog_3.html')