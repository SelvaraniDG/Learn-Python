def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulus")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponentiate(num1, num2))
    elif choice == '6':
        if num2 == 0:
            print("Error! Modulus by zero.")
        else:
            print("Result:", modulus(num1, num2))
    else:
        print("Invalid input")

calculator()
