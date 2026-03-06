print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Type S ,M ,L: " ).upper()
pepperoni = input("Do you want pepperoni? Type Y or N: ").upper()
extra_cheese= input("Do you want extra cheese?Type Y or N: ").upper()
bill = 0
if size == "S":
    bill+=12
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("Sorry, please choose either of the option")
if pepperoni == "Y":
    if size == "S":
       bill+=2
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1
print(f"Your total bill is {bill}")
