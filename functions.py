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
