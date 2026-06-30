class Car:
	def __init__(self, brand, model, price):
		self.brand = brand
		self._model = model
		self.__price = price


Car1 = Car("Benz", "G63", 100000000000)