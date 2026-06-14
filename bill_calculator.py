billAmount = int(input("Enter total bill amount:"))
numberOfPeople = int(input("Enter number of people:"))
tipPercentage = float(input("Enter tip percentage in decimals:"))

tipAmount = tipPercentage * billAmount
totalBill = billAmount + tipAmount
amountPerPerson = totalBill / numberOfPeople 

print("\n")
print("      BILL SPLIT RECEIPT      ")
print(f"Total Bill: Sh.{billAmount}")
print (f"Tip Percentage: {tipPercentage}")
print (f"Gross Amount is Sh.{totalBill} to be split between {numberOfPeople} people. ")
print (f"Amount to be paid per person: Sh.3{amountPerPerson}")
