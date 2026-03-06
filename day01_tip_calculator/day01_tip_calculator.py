print("Welcome to the tip calculator!")
bill =float(input("What was the total bill: $ "))
tip = int(input("How much tip would you like to give ? (10, 12, or 12): "))
total_people = int(input("how many people to split the bill:"))
tip_percentage  = tip/100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount
amount_per_person = total_bill / total_people

print(f"Each person should pay ${amount_per_person:.2f}")
