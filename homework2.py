#домашка2
#######
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
choice = int(input("Maximum number - press 1, minimum number - press 2, average - press 3: "))
if choice == 1:
    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number3:
        print(number2)
    else:
        print(number3)
elif choice == 2:
    if number1 < number2 and number1 < number3:
        print(number1)
    elif number2 < number3:
        print(number2)
    else:
        print(number3)
elif choice == 3:
    average = (number1 + number2 + number3)/3
    print(average)
else:
    print("Incorrect input")
meters = int(input("Enter meters: "))
choice_task2 = int(input("Convert to miles - press 1, convert to inches - press 2, convert to yards - press 3: "))
if choice_task2 == 1:
    print(f"{meters / 1609} miles")
elif choice_task2 == 2:
    print(f"{meters * 39} inches")
elif choice_task2 == 3:
    print(f"{meters * 1.094} yards")
else:
    print("Incorrect input")
print("Hello")
print("text")
print("demo")