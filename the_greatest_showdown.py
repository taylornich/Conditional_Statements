# question 1 task 1

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2

else:
    largest = num3

print("The largest number is: ", largest)


# question 1 task 2

if num1 <= num2 and num1 <= num3:
    smallest = num1

elif num2 <= num1 and num2 <= num3:
    smallest = num2

else: 
    smallest = num3

print("The smallest number is: ", smallest)

