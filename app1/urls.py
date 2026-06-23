from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_car),
    path('create/', create_car),
    path('detail/', detail_car),
    path('update/', update_car),
    path('delete/', delete_car),
    path('update-partial/', update_partial_car)
]