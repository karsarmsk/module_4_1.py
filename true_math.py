def divide(first, second):
    if second == 0:
        result = 'Ошибка'
    else:
        result = first / second
    return result

print(divide(69, 3))
print(divide(0, 7))
print(divide(49, 7))
print(divide(15, 0))
