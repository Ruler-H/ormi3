from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def test(request):
    data = [
        {'name': 'hwangbyeongheon', 'age':10},
        {'name': 'hwangbyeongheon2', 'age':20},
    ]

    s = render_to_string('main/test.html', {'data': data})
    header = '<h2>hello world</h2>'
    footer = '<h2>bye world</h2>'
    return render(request, 'main/test.html')
