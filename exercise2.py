class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restuarant = Restaurant("The Eatery", "Mexican")
print(restuarant.restaurant_name)
print(restuarant.cuisine_type)
restuarant.describe_restaurant()
restuarant.open_restaurant()