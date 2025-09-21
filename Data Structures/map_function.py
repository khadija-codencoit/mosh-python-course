#Mosh Couse Learning
items = [
    ("product1",22),
    ("product2",55),
    ("product3",10)
]

prices = list(map(lambda item : item[1],items))
print(prices)

#Problem -1
#Problem: Calculate total prices after tax for a shopping cart.You want to calculate the price after 10% sales tax for each product.

Shopping_item = [
    ("Dress",300),
    ("Shoes",400),
    ("Mackup",100)
]
price = list(map(lambda item : item[1] *1.1,Shopping_item))
print(price)