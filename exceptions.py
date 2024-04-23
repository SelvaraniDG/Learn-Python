def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Result of division:", result)
    finally:
        print("Division operation completed.")

divide(10, 2)   
divide(10, 0)
divide(12, 4)
