class Myclass:
    def __init__(self):
        self.my_list = []

    def add_item(self,item):
        self.my_list.append(item)

    def get_item(self,index):
        if 0 <= index < len(self.my_list):
            return self.my_list[index]
        else:
            return "Index out of bounds"
        
    def print_list(self):
        print(self.my_list)

my_object = Myclass()
n = int(input("Enter the number"))

for i in range(0,n):
    name = input("enter the name :")
    my_object.add_item(name)

my_object.print_list()
