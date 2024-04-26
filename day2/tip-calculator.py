#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill = float(input("Enter the total bill amount: "))

tiprate = float(input("Enter what percentage you would like to give: "))

splitnum = int(input("Enter the number of people to split the bill with: "))
tiprate_rd = round((tiprate/100)*bill, 2)

total = (bill+tiprate_rd)

total_split = total/splitnum

total_split_rd = round(total_split,2)
final_total = total_split_rd * splitnum

print(f"Each must pay {total_split_rd} for a total bill of {final_total} and tip of {tiprate_rd}")

