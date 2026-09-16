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
