# Real-Life Conditional Problem: Bus Fare Calculator

# Problem Statement:
# You are building a system for a public transport service that calculates the bus fare based on age.
# Fare Rules:
# age under 5: Free
# Age 5–12: Child Fare – ৳20
#  Age 13–59: Adult Fare – ৳40
# If the age is negative or unreasonably high (>120), print "Invalid age"

age = int(input("What is your age : "))

if age < 0 or age > 120:
    print("Invalid age")
elif age < 5:
    print("Age under 5: Free")
elif 5 <= age <= 12:
    print("Child Fare: ৳20")
elif 13 <= age <= 59:
    print("Adult Fare: ৳40")
else:  # age 60 and above
    print("Senior Fare: ৳25")