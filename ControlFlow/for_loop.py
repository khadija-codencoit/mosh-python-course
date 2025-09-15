for num in range(6):
    print("Attempt",num)


attendance = {}

# Loop through 30 students
for roll in range(1, 6):
    status = input(f"Is student {roll} present? (p/a): ").lower()
    
    # Validate input
    if status == 'p':
        attendance[roll] = "Present"
    elif status == 'a':
        attendance[roll] = "Absent"
    else:
        print("Invalid input, marking Absent by default.")
        attendance[roll] = "Absent"

# Show attendance summary
