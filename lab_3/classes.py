import math

#Task_1
class String:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

#Task_2
class Shape:
    def __init__(self):
        pass

    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self, length):
        super().__init__() 
        self.length = length

    def area(self):
        print(self.length * self.length)

#Task_3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

#Task_4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinate x: {self.x};\nCoordinate y: {self.y};")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def dist(self, other_point):
        print(math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2))

#Task_5

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money_depositied):
        self.balance += money_depositied
    def withdraw(self, money_withdrawn):
        if self.balance - money_withdrawn >= 0:
            self.balance -= money_withdrawn
        else:
            print("Not enough money")

client_1 = Account("Jim", 100)

client_1.deposit(70)
print(client_1.balance)

client_1.withdraw(70)
print(client_1.balance)

client_1.withdraw(300)
print(client_1.balance)

#Task_6

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, (int(n) // 2) + 1):
        if(n % i == 0):
            return False

    return True

#Example for me
numbers = [2, 3, 5, 7, 8, 9, 11, 13, 17, 19, 20, 23, 29, 31]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)