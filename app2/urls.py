from django.urls import path
from .views import *

urlpatterns = [
    path('list-create/', list_create_car.as_view()),
    path('update-delete-detail/', update_delete_detail_car.as_view())
]