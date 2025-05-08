num= int(input("Enter the numner: "))
def factorial(num):
    if num <2:
        return 1# -*- coding: latin-1 -*-
    else:
        return num * (factorial(num-1))
        
fact=factorial(num)
print(f"Factorial of {num} is {fact}")