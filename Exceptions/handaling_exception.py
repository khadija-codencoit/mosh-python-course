try:
    age = int(input("Age: "))
except (ValueError,ZeroDivisionError):
    print("You don't enter valid age")
else:
    print("Exection will continue")