items = [
    ("product1",22),
    ("product2",55),
    ("product3",1)
]

filtered = list(filter(lambda item :item[1]>=10,items))
print(filtered)