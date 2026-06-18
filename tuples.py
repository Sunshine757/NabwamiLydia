#create a tuple
#heterogeneous tuple
#ordered and immutable

computers = ("laptop", "desktop", "tablet", "smartphone")
print(computers)
print(type(computers))

list = ["lydia", "eva", "abby", "maria"]
print(type(list))
#converting a list to a tuple 
names = tuple(list)
print(names)
print(type(names))

#updating a tuple
#tuples are immutable so we cannot update a tuple but we can convert it to a list, update it, and then convert it back to a tuple
namesList = list(names)
namesList[0] = "Sarah"
names = tuple(namesList)
print(names)

#how to delete a tuple, first convert it to a list delete the item then convert it back
#how to concatinate
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("date", "elderberry", "fig")
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)