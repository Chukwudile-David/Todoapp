from django.urls import path
from .views import Alltodo,deleteitem,updateitem

urlpatterns =[
    path('', Alltodo, name = 'alltodo'),
    path('deleteitem/<int:pk>',deleteitem, name = 'delete'),
    path('updateitem/<int:pk>',updateitem, name = 'update')
    ]