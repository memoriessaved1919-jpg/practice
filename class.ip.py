'''CLASS deep diving
    (1) ENCAPSULATION - ichkarida yashirish va himoyalash
    (2) INHERITENCE - meros olish
    (3) POLIMORPHISM - bir nom, har xil shakl
'''

print("===== INHERITENCE =====")
# PARENT > CHILD only public & protected properties (state + method)


class Animal:  # Parent
    description = "This class is parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says:  {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "wow", True)
fish = Fish("Nemo", "zzzzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
cat.make_voice()
fish.make_voice()

print("-----")
print(Animal.description)
print(Dog.description)


print(dog.voice, fish.voice)
print("status:", fish._status)


print("===== POLIMORPHISM =====")

dog.make_voice()
cat.make_voice()

print("-----")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
print(f"result:", (a))
c = isinstance(fish, object)
result = a and b and c
print(f"the result:, {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
