#a program that uses while loop to demonstrate a bank account balance 
#the program should allow the user to deposit and withdraw money from the account until balance is zero
balance = 20000
while balance > 0:
    print("Current balance:", balance)
    action = input("Do you want to deposit or withdraw? ")
    if action == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
    elif action == "withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds.")
    else:
        print("Invalid action.")
print("Account balance is zero.")