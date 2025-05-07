class Car:
    def __init__(self,car_brand):
        self.car_brand = car_brand
    
    def show(self):
        print("my car brand is ",self.car_brand)

c = Car("ford")
c.show()