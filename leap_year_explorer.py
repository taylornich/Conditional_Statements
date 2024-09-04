# question 3 task 1

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True - The year entered is a leap year.")

else: 
    print("False - The year entered is not a leap year.")