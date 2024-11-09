from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people = [
        {'name':"abhishek", 'age':20},
        {'name':"abhi", 'age':21},
        {'name':"abhi", 'age':21}
    ]
    return render(request, 'index.html', context={'people': people})

def about(request):
 
    return render(request, 'about.html')

def contact(request):
   
    return render(request, 'contact.html')


def success(request):
    return HttpResponse("<h1>Success</h1?")

