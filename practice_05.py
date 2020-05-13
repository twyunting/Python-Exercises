def greet_user(username):
    print("Hello " + username + "!")

greet_user("Yunting")

def make_pizza(topping ='bacon'):
    """Make a single-topping pizza.""" 
    print("Have a " + topping + " pizza!") 
     
make_pizza()
make_pizza('pepperoni')

def add_number(x, y):
    return x + y

sum = add_number(89, 29)
print(sum)

class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self): 
        print(self.name + "is sitting.")   

my_dog = Dog('Peso')  

print(my_dog.name + "is a good dog !")
my_dog.sit()