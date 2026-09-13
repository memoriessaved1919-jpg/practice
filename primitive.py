print("============")
count = 100
count_type = type(count)
print(f"count: {count} count type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)
