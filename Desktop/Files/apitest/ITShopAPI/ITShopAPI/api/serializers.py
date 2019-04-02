from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, Cart, CartItem

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','first_name','last_name','email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ItemListSerializer(serializers.ModelSerializer):
    item_details = serializers.HyperlinkedIdentityField(
        view_name="api-itemdetail",
        lookup_field="id",
        lookup_url_kwarg="item_id")
    class Meta:
        model = Item
        fields = ['name','description','price','image','item_details']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CartListSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    # user=serializers.SerializerMethodField()
    ##cart_details=serializers.SerializerMethodField()
    cart_details = serializers.HyperlinkedIdentityField(
        view_name="api-cartdetail",
        lookup_field="id",
        lookup_url_kwarg="cart_id")
    class Meta:
        model = Cart
        fields = ['user','checkout','cart_details']

    # def get_user(self,obj):
    # 	return Cart.objects.filter(user=self.request.user)
    # def get_cart_details(self,obj):
    # 	return CartItem.objects.filter(cart=obj)
class ItemNameSerializer(serializers.ModelSerializer):
   class Meta:
        model = Item
        fields = ['name']


class CartDetailSerializer(serializers.ModelSerializer):
    item=ItemNameSerializer()
    class Meta:
        model = CartItem
        fields = ['item','quantity']

class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'