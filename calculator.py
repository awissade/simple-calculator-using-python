from colorama import init, Fore

init(autoreset=True)  # Initialize colorama

from operations import *

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Fore.RESET)

def main():
    print(Fore.CYAN + "+" + "-" * 43 + "+")
    print("|" + " " * 10 + Fore.YELLOW + "Simple Calculator" + " " * 10 + "|")
    print("+" + "-" * 43 + "+" + Fore.RESET)

    x = get_number_input(Fore.GREEN + "Enter the first number: " + Fore.RESET)
    y = get_number_input(Fore.GREEN + "Enter the second number: " + Fore.RESET)

    print(Fore.CYAN + "+" + "-" * 43 + "+")
    operation = input("| " + Fore.GREEN + "Enter an operation (+, -, *, /, %, ^): " + Fore.RESET)
    print(Fore.CYAN + "+" + "-" * 43 + "+" + Fore.RESET)

    try:
        if operation == '+':
            result = Add(x, y)
        elif operation == '-':
            result = Sub(x, y)
        elif operation == '*':
            result = Mul(x, y)
        elif operation == '/':
            result = Div(x, y)
        elif operation == '%':
            result = Mod(x, y)
        elif operation == '**' or operation == '^':
            result = Exp(x, y)
        else:
            print("| " + Fore.RED + "Invalid operation. " + " " * 17 + "|" + Fore.RESET)
            return

        print("| " + Fore.YELLOW + f"{x} {operation} {y} = {result:.2f}" + " " * 10 + "|")
    except ValueError as e:
        print("| " + Fore.RED + f"Error: {e}" + " " * 23 + "|" + Fore.RESET)

    print(Fore.CYAN + "+" + "-" * 43 + "+")
    ask = input("| " + Fore.GREEN + "Do you want to try again? (yes/no): " + Fore.RESET).lower()
    if ask in ["yes", "y"]:
        main()
    else:
        print("|" + " " * 41 + Fore.YELLOW + "Thanks for your time" + Fore.CYAN + " " * 2 + "|")
        print(Fore.CYAN + "+" + "-" * 43 + "+" + Fore.RESET)

if __name__ == "__main__":
    main()

