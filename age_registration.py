# Task 2: Student Age Registration
try:
    age = int(input("Enter your age: "))
    print("Age successfully recorded")
except ValueError:
    print("Invalid age entered")   # e.g. input "twenty"

print("Program ended normally.")
