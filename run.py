# Dunder = __builtins__, __init__

message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result", result)

''' "In Python, thee are builtin tools:
(1) TYPES > int, float, str, list, dict
(2) FUNCTIONS > print(), len(), input(), type(), str(), int()
(3) CONSTANTS > True, False, None, NotImplemented, Ellipsis  
'''

print(dir(__builtins__))
