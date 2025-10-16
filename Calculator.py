# Simple Python Calculator


# Getting the Operand from User
while True:
    operator = input("Enter an operator: (+ - * /) \n Note: * for multiply the numbers and / for dividing the numbers: ")
    # Check for correct input from user
    if operator not in ["+", "-", "*", "/"]:
        print(f"{operator} is not a valid operator!")
    elif operator in ["+", "-", "*", "/"]:
        break

# Getting the number
number1 = int(input("Input your first number: "))
while True:
    # Make sure that we don't get error for dividing a number to zero!
    number2 = int(input("Input your second number: "))
    if number2 == 0 and operator == "/":
        print("In division the second number can not be 0!")
    else:
        break
   
# Doing the oparation and returning the result value.     
if operator == "+":
    sum = number1 + number2
elif operator == "-":
    sum = number1 - number2
elif operator == "*":
    sum = number1 * number2
elif operator == "/":
    sum = number1 / number2

# Rounding the number to two decimal place.
sum = round(sum, 2)
# Printing the result to the console.
print(f"The result is equal to: {sum}")