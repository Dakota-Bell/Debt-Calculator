# Dakota Bell
# Budget Project 
# 03-30-2022

# Takes in your monthly income and takes a percentage and tells you what you can spend
# and how much money you should save 

# Description: Asks user how much income they make each month
# Inputs: monthly income 
# Return Value: Cash

# Desciption: Calculates gas budget
# Inputs: cash from monthly_income function
# Return Value: gas budget
def gas_budget(income):
    gas = (income * .15)
    
    return gas 

# Description: Debt calculations
# Inputs: how much debt user has
# Return Value: debt_num 
def debt_calc(income): 
    debt = input("Do you have any debt to pay off? (Y/N)")
    print()
    # If the user has debt
    if debt.upper() == 'Y':
        debt_num = float(input("How much money are you in debt? ")) 
        print()
        debt_num = (income * .12) 
        
        return debt_num 
    # Otherwise congratulate them
    else: 
        print()
        debt_num = 0 
        print("Congratulations on being debt free!") 
        return debt_num

# Description: Housing 
# Inputs: income 
# Return Value: Housing budget
def housing_calc(income):
    house_bud = (income * .35)
    return house_bud

# Description: food budget 
# Inputs: income
# Return Value: food
def food_budg(income):
    food = (income * .15)
    return food 

# Description: calculates insurance 
# Inputs: income 
# Return Value: insurance 
def insured_budg(income):
    insurance = (income * .20)
    return insurance 

# Description: calculates amount to add to savings
# Inputs: income
# Return Value: saving
def saving_acc(income): 
    saving = (income * .12)
    return saving 

# Description:
# Inputs: 
# Return Value: 
def fun_stuff(income):
    fun = (income * .03)
    return fun 

# Description: Prints out everything in either columns or in a long list
# Inputs: everysingle function
# Return Value: None
def budget_list(cash, house_bud, food, gas, insurance, saving, debt_num, fun):
    print()
    print("*****************************************")
    print()
    print("    YOUR MONTHLY BUDGET     ")
    print()
    print()
    print(f"\tYour monthly income is {cash:.2f} ")
    print()
    print(f"\tYou are in debt {debt_num:.2f} ")
    print()
    print("Your monthly expenses for: ")
    print(f"\tHousing: {house_bud:.2f}")
    print(f"\tFood: {food:.2f}")
    print(f"\tGas: {gas:.2f}")
    print(f"\tInsurance: {insurance:.2f}")
    print(f"\tSavings: {saving:.2f}")
    print(f"\tDEBT: {debt_num:.2f}")
    print(f"\tFun: {fun:.2f}")
    print()
    print("*****************************************")

def main():
    cash = float(input("What is your monthly income after taxes? "))
    print()
    
    gasoline = gas_budget(cash)

    house = housing_calc(cash)

    good_food = food_budg(cash)

    insured = insured_budg(cash)

    savings = saving_acc(cash)

    debt = debt_calc(cash)

    fun_money = fun_stuff(cash)

    budget_list(cash, gasoline, house, good_food, insured, savings, debt, fun_money)


main()