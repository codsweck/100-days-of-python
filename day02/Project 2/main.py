print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
each_pay = ((bill / person) * (1 + tip / 100))
each_pay_round = round(each_pay, 2)
print(f"Each person should pay: ${each_pay_round}")