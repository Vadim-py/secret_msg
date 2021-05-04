from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('msg/', create_msg),
    path('msg/<slug:id>/', msg_detail)
]
