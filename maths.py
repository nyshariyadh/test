def add(x, y):
    return x + y
#gyat
#gyat
def subtract(x, y):
    return x - y

def main():
    print("what opeation you like to do?")
    print("1. addition")
    print("2. subtraction")

    choice = input("please enter 1 or 2: ")

    if choice in ['1', '2']:
        try:
            num1 = int(input("enter first number: "))
            num2 = int(input("inter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("the solution is:", result)
            else:
                result = subtract(num1, num2)
                print("the solution is:", result)

        except ValueError:
            print("please enter valid numbers")
    else:
        print("invalid choice. please select 1 or 2")

if __name__ == "__main__":
    main()