'''CLASS
  (1) What is class
  (2) ordinary vs static properties
  (3) special methods
'''


print("==== What is class =====")
# class - blueprint for object creation! = object yaratish uchun shablon
# structure > state constructor method


class Person():
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}")

    @classmethod
    def explain(cls):
        print(f"static method property executed! hello")


person1 = Person("Mason", 22)
person2 = Person("Mark", 30)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("==== ordinary vs static properties =====")
# static state

new_message = Person.message
print("new_message", new_message)

# static method

Person.explain()


print("==== special/magic methods =====")
# Python's most common spetial methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__


class Car():
    # state

    description = "This class makes cars"

    # constructor

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method

    def start_engine(self):
        print(f"The {self.name} started engine")

    def stop_engine(self):
        print(f"The {self.name} stopped engine")

    def __str__(self):
        return f" {self.name} was produced in {self.year} years! "

    def __call__(self, *args, **kwds):
        print("Object called as function")   # call like function
        return True


my_car = Car("Tracker", 2026)
print(my_car)
my_car.start_engine()
my_car.stop_engine()

print("========")
your_car = Car("Cobalt", 2023)
print(your_car)

responce = my_car()
print("responce:", responce)    # call like a function
your_car()
