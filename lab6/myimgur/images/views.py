from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    return render(request, 'images/homepage.html', context)

def image_list(request):
    context = {}
    return render(request, 'images/image_list.html', context)