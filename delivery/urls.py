from .views import get_location_view, select_location_view, save_location
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, RestaurantViewSet, MenuViewSet, MenuItemViewSet, OrderViewSet, OrderItemViewSet, DeliveryViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'deliveries', DeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-location/', get_location_view, name='get_location'),
    path('select-location/', select_location_view, name='select_location'),
    path('api/save-location/', save_location, name='save_location'),
]
