from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItemsViewSet

app_name = 'items'

api_items_router_v1 = DefaultRouter()
api_items_router_v1.register(r'items', ItemsViewSet, basename='items')

urlpatterns = [
    path(r'', include(api_items_router_v1.urls)),
]
