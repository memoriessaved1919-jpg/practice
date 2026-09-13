'''FUNCTIONS
(1) Define va Call 
(2) Paramentr va Argument
(3) Keyword va Default argumentlari
(4) Scope 
'''
print("====== Define(parametr) va Call(argument)  ======")
# build-in function > print() type()
# Function - biror bir operatsiyani amalga oshirib beradigon kod blok
# (Function - reusable blobk of code)
# Instead of block {} in JAVA ,  Python uses indentation :


# DEFINE - build (parametr)
def greet(a):
    print(f"how do you do {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute (argumet)
result1 = greet('Matt')
print("result1:", result1)

result2 = greeting('Mason')
print("result2:", result2)


print("====== Keyword va Default argumentlari ======")
# DEFINE


def give_greet(name, age=30):
    print("give_greet is executed")
    return f"Hi {name} are you really {age} yars old ?"


# CALL
result3 = give_greet(name="Mark", age=22)
print("result3:", result3)

result4 = give_greet("Joni")
print("result4:", result4)

print("====== Scope ======")
