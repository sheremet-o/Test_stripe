from django.contrib import admin
from django.urls import include, path


api_patterens = [
    path('', include('items.urls', namespace='api_items'),)
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterens)),
]
