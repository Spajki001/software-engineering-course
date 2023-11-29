from django.urls import path
from .views import image_list
from .views import image_detail
from .views import create_image

app_name = 'images'
urlpatterns = [
    path('', image_list, name='list'),
    path('<int:image_id>', image_detail, name='detail'),
    path('new/', create_image, name='create'),
]