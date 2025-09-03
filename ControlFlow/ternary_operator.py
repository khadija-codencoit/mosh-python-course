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


