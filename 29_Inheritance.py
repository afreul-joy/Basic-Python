class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f" brand {self.brand} , price : {self.price} ")


firstMoble = Mobile("iphone","1000")
firstMoble.display()