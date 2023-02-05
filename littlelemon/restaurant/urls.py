from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_detail'),
    path('restaurant/booking/', include(router.urls)),
]
