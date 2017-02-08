class Products(object):
    def __init__(self, name, quantity, price):
    	self.name = name
    	self.quantity = quantity
    	self.price = price


    def product_price_calc(self, price, quantity):
    	total_price = self.price * self.quantity
    	return total_price

class Product_by_weight(Products):
	def __init__(self, name, weight, price):
	    super().__init__(name, price)
	    self.weight = weight
    

class Product_by_unit(Products):
    pass

class Product_by_volume(Products):
    pass

w1 = Product_by_weight('meat', 2, 200)
print(w1.name, w1.quantity, w1.price)

print(w1.product_price_calc(w1.price, w1.quantity))
