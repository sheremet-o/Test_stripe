from django.urls import path

from . import views


app_name = 'items'

urlpatterns = [  
    path('item/<int:item_id>', views.item_detail, name='item_detail'),
    path('config/', views.stripe_config),
]
