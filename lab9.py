#sets-data structures
cars = {"suzuki", "toyota", "benze"}
print(cars)
print(type(cars))

#accesing datain a set
#methods
#use of the add() method to add an item to a set
cars.add("Mazda")
print(cars)

#union method combines sets and returns a set that contains all items from both sets
ages= {29, 30, 25, 22 ,"suzuki"}
w = cars.union(ages)
print(w)
print(type(w))

#intersection method retruns a set that conatains only theitems tahts
#are common to both sets
i = cars.intersection(ages) 