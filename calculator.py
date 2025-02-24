print("Calculator")
print("Welcome to the Calculator!")

print("Enter the first number you want to calculate")
first_number = float(input())

print("Enter the second number you want to calculate")
second_number = float(input())

print("Enter 'o' to choose the operation you want to calculate")
operation = input().lower()

if operation == "o":
    print("Enter 'a' for addition")
    print("Enter 's' for subtraction")
    print("Enter 'm' for multiplication")
    print("Enter 'd' for division")
    op = input().lower()

    if op == "a":
        print(first_number + second_number)
    elif op == "s":
        print(first_number - second_number)
    elif op == "m":
        print(first_number * second_number)
    elif op == "d":
        if second_number != 0:
            print(first_number / second_number)

print("Thank you for using the calculator")
print("Enter 'c' to check the credits")

next_action = input().lower()

if next_action == "c":
    print("This calculator was made by Neehal")
else:
    print("Invalid input for next action.")