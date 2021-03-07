x = int(input("Enter the number of grades: "))
y = 0
b = 1
g = 0

print()

for h in range(x):

    z = int(input("Type your " + str(b) + " grade here: "))
    b = b + 1
    y = y + z

y = (y + z) / x
print()
print("Your final grade is: " + str(y))