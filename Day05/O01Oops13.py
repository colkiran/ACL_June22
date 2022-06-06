
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return f"The price is :{self.__price}"

    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be negative....")
        else:
            self.__price = val

import sys
try:
    pepsi = Product(45)
    print(pepsi.get_price())
    pepsi.set_price(60)
    print(pepsi.get_price())

except:
    print("Exception raised.....")
    print(sys.exc_info()[0], "Occured")
    print(sys.exc_info()[1])

