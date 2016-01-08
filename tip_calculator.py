mealPrice=input("How much did your meal cost?")
tip=input("How much would you like to tip?")
tax=input("How much is the tax?")

finalAmount=(mealPrice * tip)+(mealPrice*tax)+(mealPrice)

print 'The final amount for your meal is $', finalAmount
