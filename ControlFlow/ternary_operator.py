age = 22

if age >= 18:
    message = "Eligible"
else :
    message = "Not Eligible"
print(message)


#Ternary Operator
message = "Eligible" if age >= 18 else  "Not Eligible" #<result_if_true> if <condition> else <result_if_false>
print(message)


#2. Voting Eligibility

user_age = int(input("Enter your age : "))

text = "Eligible" if user_age >= 18 else "Not Eligible"
print(text)

## 3. Login System
# Input: Username and password
#Check if they match stored values: "admin", "1234"
# Output: "Login successful" or "Access denied"

correct_user = "admin"
correct_password = 12345

username = input("Enter username : ")
password = int(input("Enter your password : "))

message = "Login successful" if username == correct_user and password == correct_password else "Access denied"
print(message)


