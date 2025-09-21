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

#Problem-2
#Convert temperatures

celcius = [10,2,3,4]
fahrenheit = list(map(lambda c :  c * 9/5 + 32,celcius))
print(fahrenheit)

#Problem -3
#Extract emails from user data

users = [("khadija", "khadija@example.com"), ("Bob", "bob@example.com")]
emails = list(map(lambda item :item[1],users))
print(emails)