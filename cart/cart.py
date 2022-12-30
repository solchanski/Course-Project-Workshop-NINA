from decimal import Decimal
from django.conf import settings
from store.models import Item


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'amount': 0, 'price': str(item.price)}
            self.cart[item_id]['amount'] = 1
        else:
            if self.cart[item_id]['amount'] < 100:
                self.cart[item_id]['amount'] += 1

        self.save()

    def update(self, item, quantity):
        item_id = str(item.id)
        self.cart[item_id]['amount'] = item

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['amount']
            yield item

    def __len__(self):
        return sum(item['amount'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['amount'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
