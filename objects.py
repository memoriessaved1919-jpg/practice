'''OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system
'''


import array  # package/module
import math
print("=========")


# An object has state and method properties
# Everything is object in Pythonss


print(type("Hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigms > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheitance | Polimorphism

result1 = math.ceil(98.7)  # CALL
print("resulrt1:", result1)


print("===== Error handling system =====")
car_dict = dict(name="tayota", year=2026, electric="True")


try:
    print("passed here")
    result = car_dict.speed
    print(f"result:", result)
except KeyError as err:
    print("No origin state property found", err)
except AttributeError as err:
    print("No origin state property found", err)
else:
    print("executed successfully without errors")
finally:
    print("Final closing logic")
