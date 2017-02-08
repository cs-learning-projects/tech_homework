class Abstract_product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Purchase_price_total(object):
    #def __init__(self):
    #    self.products = []

    def product_price_calc(self, name, price, quantity):
        total_price = price * quantity
        print(total_price, quantity)
        return total_price
    

class Product_by_weight(Abstract_product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    

class Product_by_unit(Abstract_product):
    #def __init__(self, name, price, unit):
    #    super().__init__(name, price)
    #    self.unit = unit
    pass

class Product_by_volume(Abstract_product):
    #def __init__(self, name, price, volume):
    #    super().__init__(name, price)
    #    self.volume = volume
    pass

w1 = Product_by_weight('meat', 200, 2)
print(w1.name, w1.weight, w1.price)
c = Purchase_price_total()
c.product_price_calc(w1.name, w1.price, w1.weight)

