import math
def divide(first, second):
    if second == 0:
        z = math.inf
    else:
        z = first / second
    return z

# print(divide(69, 3))
# print(divide(3,0))
# print(divide(49, 7))
# print(divide(15,0))