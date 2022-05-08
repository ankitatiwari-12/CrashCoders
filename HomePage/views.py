from django.shortcuts import render

def home_page(request):
    return render(request, "index.html")

def explore(request):
    return render(request, "info.html")

# Create your views here.
