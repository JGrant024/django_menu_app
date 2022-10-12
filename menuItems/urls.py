from django.urls import path

from .views import MenuItemListAPIView

urlpatterns = [

    path('menu_items/', MenuItemListAPIView.as_view())
]
