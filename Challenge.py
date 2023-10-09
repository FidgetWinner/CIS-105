
Expenses = {}
while(True):
    tempType = str(input("Enter the type of expense(enter e to exit): "))
    if(tempType == 'e'):
        break
    tempCost = float(input("Enter expense cost: "))
    Expenses.update({tempType: tempCost    })

print(Expenses)
monthlyExpenses = sum(Expenses.values())
print("Your total monthly expenses are: ", monthlyExpenses)