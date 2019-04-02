from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView
from .serializers import (ItemListSerializer, ItemDetailSerializer,UserCreateSerializer,
	UserDetailSerializer,CartListSerializer,CartDetailSerializer,CartItemCreateUpdateSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.auth.models import User
from .models import Item, Cart, CartItem
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','description','price','category']


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class CartListView(ListAPIView):
    serializer_class = CartListSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user,checkout=0)

class CartDetailView(ListAPIView):
	#queryset = CartItem.objects.all()
	serializer_class = CartDetailSerializer
	permission_classes = [IsAuthenticated,IsOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'cart_id'

	def get_queryset(self):
		cart = self.kwargs['cart_id']
		return CartItem.objects.filter(cart=cart)

class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated,IsOwner]

class CartItemUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'
    permission_classes = [IsAuthenticated,IsOwner]

class ProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'