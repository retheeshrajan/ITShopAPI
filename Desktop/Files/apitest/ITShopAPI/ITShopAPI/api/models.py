from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100,null=True, blank=True)
    quantity=models.IntegerField(default=1)

    def __str__(self):
    	return self.name

    
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	checkout = models.IntegerField(default=0)

	def __str__(self):
		return 'Cart #' + str(self.id) + ' for ' + self.user.username


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
    	return 'Items in cart #' + str(self.cart.id) + ' for ' + self.cart.user.username