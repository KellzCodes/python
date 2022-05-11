numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    numerator = float(numerator)
except Exception as e:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
except Exception as e:
    print("The denominator is not a number.")


try:
    result = numerator / denominator
    print(f"The result of this division is {result}.")
except ZeroDivisionError as e:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print('Goodbye!')
