from django.shortcuts import render
from .models import Image

# Create your views here.

def homepage(request):
    count = Image.objects.count()
    context = {
        'count': count,
    }
    return render(request, 'images/homepage.html', context)

def image_list(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'images/image_list.html', context)