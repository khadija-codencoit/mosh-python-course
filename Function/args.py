def multiply(*numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total




print(multiply(3, 5, 6, 7))
