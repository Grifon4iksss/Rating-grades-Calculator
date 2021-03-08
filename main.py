numberGrades = int(input("Enter the number of grades: "))
y = 0 # Sum of all grades
b = 1 

print()

for h in range(numberGrades):

    z = int(input("Type your " + str(b) + " grade here: "))
    b = b + 1 # show how many times was z called
    y = y + z

y = y / numberGrades # Calculation

print()
print("Your final grade is: " + str(y))
