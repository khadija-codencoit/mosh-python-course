numbers = [3,51,3,4,77,8,9]
#numbers.sort(reverse=True)
print(sorted(numbers,reverse=True))
print(numbers)

items = [
    ("product1",10),
    ("product1",1),
    ("product1",123)
]

def sort_item(item):
    return item[0]

items.sort(key = sort_item)
#items.sort(key=lamda item:item[1])
print(items)

# Problem - 1
# You have employee data with name and salary:
# Sort employees based on salary.
# Print the highest-paid employee.

Employee = [
    ("Tamim",20000),
    ("Sakib",50000),
    ("Masrafi",40000)
]

def sort_item(item):
    return item[1]

Employee.sort(key=sort_item)
print(Employee)