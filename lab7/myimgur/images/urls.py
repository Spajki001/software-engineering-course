from django.urls import path
from .views import image_list
from .views import image_detail
from .views import create_image

urlpatterns = [
    path('', image_list, name='image_list'),
    path('<int:image_id>', image_detail, name='image_detail'),
    path('new/', create_image, name='create_image'),
]