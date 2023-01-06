from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from store.models import Item


class Time(models.Model):
    from_time = models.TimeField(default=timezone.now)
    to_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.from_time} - {self.to_time}")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', default=0)
    # phone = models.CharField(max_length=12)
    address = models.CharField(max_length=40, default="Gagarina street, 55")
    date = models.DateField(default=timezone.now)
    delivery_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='order_delivery_time', default=0)
    status = models.BooleanField()

    def __str__(self):
        return str(f"{self.user} {self.address} {self.date} {self.delivery_time} {self.status}")

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order', default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=0)
    amount = models.IntegerField(default=1)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(f"{self.amount}")

    def get_total_cost(self):
        return self.item.price * self.quantity
