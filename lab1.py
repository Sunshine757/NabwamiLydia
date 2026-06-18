#programm
number = 90
count = 0
while count <3:
 guess = int(input("guess the number"))
 if guess == number:
  
  print("you are correct")
  break
 else:
  count +=1
  print ("wrong number try again")
  if count == 3:
  
   print(f"correct number is {number}")















































   