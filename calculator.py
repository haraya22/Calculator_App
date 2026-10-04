# simple calculator project (from scratch)
# Define the operations
# handle dividing by zero error
# while statement for selected operation
# the if statements of user input
# Try function for num1 and num2, then a except ValueError incase of character that is not a number
# if and elif statements for each choice
# else invalid number variable so try again!
# print out calculator


def add(x, y): 
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        return ("Error! Cannot divide by zero!")
    return x / y

def mul(x, y):
    return x * y

def calculator():
    print("SIMPLE CALCULATOR!")

    while True:
        print("\nSelect an Operation:")
        print("1. +")
        print("2. -")
        print("3. /")
        print("4. *")
        print("5. exit")

        choice = input("Enter choice (1-5): ")

        # If user wants to quit check the condition
        if choice == '5':
            print("Goodbye!")
            break

        # Check other choices
        if choice in('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid number(s), please try again!")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} / {num2} = {div(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} * {num2} = {mul(num1, num2)}") 
        else:
            print("Invalid choice, please try again with options 1 - 5...")

if __name__ == "__main__":
    calculator()