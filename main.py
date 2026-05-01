import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return  n1*n2

def div(n1, n2):
    return n1/n2

operation_dictionary = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    print(art.logo)
    num_1 = float(input("Enter the first number: "))
    should_continue = True
    while should_continue:
        operation = input("Pick an operation.\nType '+', '-', '*' or '/' :  ")
        num_2 = float(input("Enter the second number: "))
        answer = operation_dictionary[operation](n1=num_1, n2=num_2)
        print(f"{num_1} {operation} {num_2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'q' to quit.\n ").lower()
        if choice == "y":
            num_1 = answer
        elif choice == "n":
            should_continue = False
            print("\n" * 30)
            calculator()
        else:
            should_continue = False

calculator()

