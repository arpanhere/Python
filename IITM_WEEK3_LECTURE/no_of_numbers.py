number = abs(int(input("Enter the number: ")))
digits = 1
while(number >9):
    number = number //10
    digits = digits+1
print("The number of numbers is",digits)