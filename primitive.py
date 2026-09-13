print("====== number ======")
count = 100
count_type = type(count)
print(f"count: {count} count type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("====== string ======")

# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"The type of course: {result}")
result = course.title()
print(f"The title: {result}")
result = course.upper()
print(f"title upper: {result}")
result = course.replace("Python FullStack", "Engineering")
print(f"title replace: {result}")
