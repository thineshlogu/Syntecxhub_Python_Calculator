# Simple Calculator
# Syntecxhub Internship - Project 1


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Main Program
while True:

    print("\n===== SIMPLE CALCULATOR =====")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("C Clear")
    print("Exit")

    operator = input("\nChoose operator: ")

    if operator.lower() == "exit":
        print("Thank you!")
        break

    elif operator.lower() == "c":
        print("Calculator cleared!")
        continue

    elif operator in ["+", "-", "*", "/"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        if operator == "+":
            result = add(num1, num2)

        elif operator == "-":
            result = subtract(num1, num2)

        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)

        print("Result:", result)

    else:
        print("Invalid operator!")