Monthly_income = int(input("Enter your monthly income: "))
Monthly_expanses = int(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_income - Monthly_expanses
interest = 0.05
projected_savings = Monthly_savings * 12 + (Monthly_savings * interest)
print("Your monthly savings are ",Monthly_savings)
print("Projected savings after one year, with interest,is",projected_saving)