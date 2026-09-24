'''OPERATORS & CONDITIONS
    (1) Operators
    (2) Conditions
    (3) Logical Operators
'''
print("======= Operators =======")
# + - > >= < <= * /     // % += -= ** ==

# == faqat valueni solishtiradi

# is faqat referanceni solishtirdi

a = 19
b = 5
print(a / b)
result = a // b
left = a % b
print(f"the result: {result}, the left {left}")

a += 100
print("a", a)

print("b*b:", b**2)
print("b*b*b:", b**3)

print("D"*5)


c = dict(name="Mason", age=22)
d = dict(name="Mason", age=22)
e = c

# == faqat valueni solishtiradi
print("c == d", c == d)  # only value
print(id(c), id(d), id(e))

# is faqat referanceni solishtirdi
print("c is d", c is d)
print("c is e", c is e)


print("======= Condtions =======")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("======= Logical Operators =======")

age = 20
# person = None

# if age > 16:
#     person = "Adult"
# else:
#     person = "child"

# print("person:", person)

# Ternary operator

person = "Adult" if age > 18 else "child"
print("person:", person)

print("--------")

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, do you want to be student! ")
elif is_admin:
    print("Please go to this Office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")

#    or = True + False = True
#    and = True + False = False
