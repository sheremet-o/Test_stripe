from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter


app_name = 'stripe_api'

api_items_router_v1 = DefaultRouter()
api_items_router_v1.register(r'items', views.ItemsViewSet, basename='items')

api_patterens = [
    path('', include('items.urls', namespace='api_items'),)
    
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterens)),
]
