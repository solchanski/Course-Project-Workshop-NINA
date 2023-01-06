from django.db import models


class Type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Item(models.Model):
    name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='./static/image')
    price = models.IntegerField(max_length=10, default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='item_type', default=0)

    def __str__(self):
        return str(f"NAME:{self.name} IMAGE:{self.image} PRICE:{self.price} BYN TYPE:{self.type}")
