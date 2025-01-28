# calucate expression
import math

def evaluate_expression(x, y, z):
    return 4 * (x**4) + 3 * (y**3) + 9 * z + 6 * math.pi

# Taking user inputs
x = float(input("Enter value of X: "))
y = float(input("Enter value of Y: "))
z = int(input("Enter value of Z: "))

# Calculating result
result = evaluate_expression(x, y, z)

# Printing result
print(f"The result of the expression is {result}")

# mins and second
a = int (input("Enter the seconds :"))
seconds = a

minutes, remaining_seconds = divmod(seconds, 60) 

print(f"{seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds")

# reversed number
a = int(input("Enter the value of a :"))
number = a
reverse= int(str(number)[::-1])
print(reverse)

# Day of the year

day = int(input("Enter the Day :"))
month = int(input("Enter the month :"))
days_inmonth=30
Dayoftheyear = (month - 1)*(days_inmonth + day)

print ("Day of the year:",Dayoftheyear)

# Good after noon

name = str(input("Enter name :"))

print(f"{name} \nGood afternoom")

# Fill leter

name = str(input("Enter name :"))
Date = int ((input("Enter Date :")))

print(f"Dear {name} \nyour are selected! \n{Date}")

# double space in a string

string = "Alok  "
 
print(len(string))

# replace double space with single in string

string = "Alok "

print(len(string))

# escape squeences

letter = "Dear Harry, \tThis python \ncoures is //nice thanks!"

print(letter)



