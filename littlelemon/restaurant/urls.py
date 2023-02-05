from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_detail'),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
