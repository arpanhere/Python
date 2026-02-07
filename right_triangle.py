n = int(input("Enter the no. of rows: "))
for i in range(n):
    for j in range(n):
        if i ==j or i == n-1 or i>=j:
            print("*", end = ' ')
        else:
            print("", end = "")
    print( )