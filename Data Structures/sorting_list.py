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
print(items)