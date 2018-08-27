import operator

class Item(object):
    def __init__(self, quantity, measure, name, price):
        self.quantity = quantity
        self.measure = measure
        self.name = name
        self.price = float(price)

    def __str__(self):
        return "{0:5} {1:<6}{2:<10} @ ${3:.<6}${4:<2.2}".format(
            self.quantity, self.measure, self.name, self.price, self.quantity * self.price)


class Cart(object):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __format__(self, code):
        if code == 'short':
            return ', '.join([one_item.name
                              for one_item in sorted(self.items,
                                                     key=operator.attrgetter('name'))])
        elif code == 'xlong':
            return '\n'.join(['\t' + str(one_item)
                              for one_item in sorted(self.items,
                                                     key=operator.attrgetter('name'))])

        else:
            return 'unknown format code {0}'.format(code)


cart = Cart()
cart.add(Item(1.5, 'kg', 'tomatoes', 5))
cart.add(Item(2, 'kg', 'cucumbers', 4))
cart.add(Item(1, 'tube', 'toothpaste', 2))
cart.add(Item(1, 'box', 'tissues', 4))

print("Your cart contains: {0:short}".format(cart))
print("Your cart:\n{0:xlong}".format(cart))
