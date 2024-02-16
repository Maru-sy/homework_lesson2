try:
    user_select = int(input("Enter day number: "))
    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect day number")
except ValueError as error:
    print(f"Enter only integer numbers,please.")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End")
try:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    if not number1 == number2:
        if number1 > number2:
            print(number2, number1)
        else:
            print(number1, number2)
    else:
        print("Equal numbers entered")
except ValueError as error:
    print(f"Enter only integer numbers,please.")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End")
try:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    operation = input("Enter mathematical operation +-/*: ")
    match operation:
        case "+":
            print(f"Result: {number1 + number2}")
        case "-":
            print(f"Result: {number1 - number2}")
        case "*":
            print(f"Result: {number1 * number2}")
        case "/":
            print(f"Result: {number1 / number2}")
        case _:
            print("Incorrect operation enter")
except ValueError as error:
    print(f"Enter only integer numbers,please.")
    print(f"ValueError: {error}")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End")








