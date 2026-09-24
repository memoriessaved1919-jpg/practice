'''LOOP Operations
   (1) for - Bergilangan tartibda ishga tushadi misol: "MIT" faqat 3 marta loop bo'ladi 
   (2) break/else
   (3) while - nechi marta loop bo'ishi nomalum hollarda ishlatiladi
'''
print("===== for operator =====")
# Iterable objects > string, dict, turple, list, range, map, filter
text = "MIT"
numbs = [10, 7, 3, 4]  # list
car_obj = dict(brand="ferrari", year=2025)  # dict
range_obj = range(5)  # range (0, 5)

for letter in text:
    print(f"the letter: {letter}")

print("-------")

for numbers in numbs:
    print(f"the number: {numbers}")

print("-------")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")


print("===== break/else =====")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached BREAK")
        break
else:
    print("Looped successfully")

print("===== while operator =====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the number equals {numb}")

print("-------")
count = 0
while True:
    count += 1
    x = int(input("Find number"))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong, please try again")
