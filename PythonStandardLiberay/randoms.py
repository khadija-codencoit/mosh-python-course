import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choices([2,88,9,7,6],k=2))
print("".join(random.choices("kjgfdsasdfg",k=2)))
print("".join(random.choices(string.ascii_letters + string.digits,k=5)))
print("".join(random.choices(string.ascii_letters + string.digits,k=9)))