from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path(
        'create-checkout-session/<pk>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session')
]
