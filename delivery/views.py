from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import LocationSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Address, Restaurant, Menu, MenuItem, Order, OrderItem, Delivery
from .serializers import AddressSerializer, RestaurantSerializer, MenuSerializer, MenuItemSerializer, OrderSerializer, OrderItemSerializer, DeliverySerializer
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def save_location(request):
    logger.debug(f"Request data: {request.data}")
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        try:
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']
            accuracy = serializer.validated_data.get('accuracy', None)

            logger.debug(f"Validated data - Latitude: {latitude}, Longitude: {longitude}, Accuracy: {accuracy}")

            address, created = Address.objects.get_or_create(user=request.user)
            address.latitude = latitude
            address.longitude = longitude
            address.accuracy = accuracy
            address.save()

            return Response({"message": "Location saved successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error saving location: {e}")
            return Response({"error": "An error occurred while saving the location."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        logger.debug(f"Serializer errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_location_view(request):
    return render(request, 'orders/get_location.html')


def select_location_view(request):
    return render(request, 'orders/select_location.html')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
