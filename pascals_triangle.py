from math import factorial
# To get number of rows
row = int(input())

for i in range(row):
    # For spacing 
    print(" " * (row-i), end= "")
    for j in range(0,i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print() 