print("===== Iterable objects & RANGE =====")
# Iterable objects > string, dict, turple, list, range, map, filter

range_obj = range(3)
print("range_obj", range_obj)


for letter in "MIT":
    print(f"the letter {letter}")

for ele in range_obj:
    print(f"ele:", ele)

print("===== DICTIONARY =====")
# Dictionary is JSON object!
person = {"name": "justin", "age": 25, "single": "True"}
person_obj = dict(name="Justin", age=25, single="True")

print(f"{person}")
print(f"{person_obj}")

name = person_obj["name"]
print(f"{name}")

name3 = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)

print(f"name: {name3}, hobby: {hobby}, balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"key) > value {person_obj.get(key)}")
