class User:
    def __init__(self,username):
        self.username = username
    
    def update_name(self,new_name):
        self.username = new_name

    def display(self):
        print("HI BOSS ",self.username)

u = User("Kamran")
u.display()
u.update_name("Ali")
u.display()