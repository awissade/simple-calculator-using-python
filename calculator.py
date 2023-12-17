from Operations import *

def main():
    print("     This is a simple calculator     ")
    print("-------------------------------------------")
    print("? ? ? = ?")
    print("-------------------------------------------")
    x = float(input("Enter the first number : "))
    print("-------------------------------------------")
    print(x, "? ? = ?")
    print("-------------------------------------------")
    y = float(input("Enter the second number : "))
    print("-------------------------------------------")
    print(x, "?", y, "= ?")
    print("-------------------------------------------")
    operation = str(input("Enter one of this operations (+,-,*,/,%,^) : "))
    print("-------------------------------------------")
    if operation == '+':
        print(x, operation, y, "=", Add(x, y))
        print("-------------------------------------------")
    elif operation == '-':
        print(x, operation, y, "=", Sub(x, y))
        print("-------------------------------------------")
    elif operation == '*':
        print(x, operation, y, "=", Mul(x, y))
        print("-------------------------------------------")
    elif operation == '/':
        print(x, operation, y, "=", Div(x, y))
        print("-------------------------------------------")
    elif operation == '%':
        print(x, operation, y, "=", Mod(x, y))
        print("-------------------------------------------")
    elif operation == '**' or operation == '^':
        print(x, operation, y, "=", Exp(x, y))
        print("-------------------------------------------")
    else:
        print("There is an error in the operation chosing")
        print("-------------------------------------------")

    ask = str(input("Do you want to try again? "))
    if ask.upper() == "YES" or ask.upper() == "Y":
        main()
    else:
        print("Thanks for your time")
        return 0

main()
