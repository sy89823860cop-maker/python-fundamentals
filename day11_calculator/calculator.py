import art
def add (n1 ,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2
operation={
   "+":add,
   "-":subtract,
   "*":multiply,
    "/":divide
}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("Enter the first number: "))
    while should_continue:

        for symbol in operation:
            print(symbol)
        operation_symbol=input("Type the operation to perform:")
        num2 = float(input("Enter the next number: "))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        want_continue= input("Do you want to continue This calculation type y for yes and n for no :")
        if want_continue=="n":
            should_continue = False
        else:
            num1= answer
calculator()
