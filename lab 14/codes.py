# class Car:
#     # Constructor to initialize the object
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute

#     # Method to describe the car
#     def car_details(self):
#         return f"Car: {self.brand}, Model: {self.model}"

# # Creating an object of the Car class
# my_car = Car("Toyota", "Corolla")
# print(my_car.car_details())  


# # Class with Methods and Attributes
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     # Method to calculate area
#     def area(self):
#         return self.width * self.height

#     # Method to calculate perimeter
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# # Create an object
# rect = Rectangle(10, 5)

# # Accessing methods
# print(f"Area: {rect.area()}")  # Output: Area: 50
# print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30



# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance

# # Create an account
# account = BankAccount("John", 1000)
# account.deposit(500)
# print(account.get_balance())  # 
# account.withdraw(700)
# print(account.get_balance())  # 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I am an animal."

# # Dog class inherits from Animal class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# # Cat class inherits from Animal class
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  # 
# print(cat.speak())  # 


# class Polygon:
#     # method to render a shape
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     # renders Square
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     # renders circle
#     def render(self):
#         print("Rendering Circle...")
    
# # create an object of Square
# s1 = Square()
# s1.render()

# # create an object of Circle
# c1 = Circle()
# c1.render()

# from abc import ABC, abstractmethod

# # Abstract class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# circle = Circle(5)
# print(f"Area of the circle: {circle.area()}")  # 

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# circle1 = Circle(5)
# print(f"Circle 1 - Radius: {circle1.radius}, Area: {circle1.area()}, Perimeter: {circle1.perimeter()}")

# circle2 = Circle(3)
# print(f"Circle 2 - Radius: {circle2.radius}, Area: {circle2.area()}, Perimeter: {circle2.perimeter()}")


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}")

    def apply_discount(self, discount_percent):
        self.price *= (1 - discount_percent / 100)

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 25.99)
book1.display_details()

book2 = Book("To Kill a Mockingbird", "Harper Lee", 19.95)
book2.display_details()

book1.apply_discount(10)
print(f"Discounted price for {book1.title}: ${book1.price:.2f}")