from django.shortcuts import render
from .models import Image
from django.http import HttpResponse

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

def image_detail(request, image_id):
    image = Image.objects.get(id=image_id)
    context = {
        'image': image,
    }
    return render(request, 'images/image_detail.html', context)