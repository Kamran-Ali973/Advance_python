class car:
    def __init__(self,brand):
        self.brand = brand

    def rename(self,rename):
        self.brand = rename
    
    def show(self):
        print("this the car brand ",self.brand)

c = car("Ford")
c.show()
c.rename("Sabru")
c.show()