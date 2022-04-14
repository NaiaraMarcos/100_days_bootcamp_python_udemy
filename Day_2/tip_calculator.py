#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("Welcome to the tip calculator!")
amount_bill = input("What was the total bill? ")
tip_percent = input("How much tip would you like to give? 10, 12 or 15? ")
n_people = input("How many people to split the bill? ")

amount_float = float(amount_bill[1:])
tip_percent_float = float(tip_percent)
n_people_int = int(n_people)

total_bill = (amount_float * tip_percent_float/100) + amount_float
total_bill_person = round(total_bill / n_people_int, 2)
total_bill_person = "{:.2f}".format(total_bill_person)

print(f"Each person should pay: $ {total_bill_person}")
