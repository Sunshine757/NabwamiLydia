#creating a list
a =[1, 2, 3, 4, 5]
print(a)  
print(type(a))


Food = ["pizza", "burger", "tacos"]
print(Food)
print(type(Food))


#accesinga an item in a list
print(Food[0])  # prints the first item in the list
print(Food[1])  # prints the second item in the list
print(Food[2])  # prints the third item in the list

#use of  a constructor 
Cars = list(("suxuki", "toyota", "honda"))
  
#use of the remove() to remove an item from a list
Food.remove("tacos")

#pop()
removedFood = Food.pop(Food[2])
print(removedFood)

#add items to a list using the append()method
Food.append("pasta")
print(Food)
#add an item at a specific location using the insert()method
Food.insert(1, "Kaalo")

#update items in a list
Food[0] = "rice"
print(Food)

#nested lists
matrix = [[1,2,3], [4,5,6]]
print(matrix)
print(matrix[0][2])

for row in matrix:
    for column in row:
        print(column)