import webbrowser
import time

print("welcome")
webbrowser.open("http://facebook.com")



#Problem-1
socile_median = ['facebook','youtube']

for index  , i in enumerate(socile_median,start=1):
    print(f"{index} {i}")

choice = input("Give your choice 1,2 : ")

if choice == 1:
    webbrowser.open("http://facebook.com")
else:
    webbrowser.open("http://youtube.com")