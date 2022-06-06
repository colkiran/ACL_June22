
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("Getter called......")
        return f"The price is :{self.__price}"

    def set_price(self, val):
        print("Setter called.....")
        self.__price = val

    def del_price(self):
        print("Deleter called......")
        self.__price = 0

    price = property(get_price, set_price, del_price)

Coke = Product(65)
print(Coke.price)
Coke.price = 80
del Coke.price
print(Coke.price)

