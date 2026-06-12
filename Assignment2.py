def calculateFinalPrice(subtotal, couponCode, location):
	discount = 0

	if subtotal >= 500:
		discount = 0.20
	elif subtotal >= 200:
		discount = 0.10
	elif subtotal >= 100:
		discount = 0.05

	couponCode = couponCode.upper()
	if couponCode == "SAVE10":
		discount += 0.10
	elif couponCode == "SAVE5":
		discount += 0.05
	elif couponCode != "NONE":
		print("Invalid coupon code. No extra coupon discount applied.")

	if discount > 0.30:
		discount = 0.30

	if location.lower() == "uganda":
		taxRate = 0.18
	elif location.lower() == "kenya":
		taxRate = 0.16
	else:
		taxRate = 0.15

	discountAmount = subtotal * discount
	priceAfterDiscount = subtotal - discountAmount
	taxAmount = priceAfterDiscount * taxRate
	finalPrice = priceAfterDiscount + taxAmount

	return discountAmount, taxAmount, finalPrice


def login():
	users = {
		"admin": {"password": "admin123", "role": "Admin"},
		"customer": {"password": "cust123", "role": "Customer"},
		"cashier": {"password": "cash123", "role": "Cashier"},
	}

	username = input("Enter username: ").lower()
	password = input("Enter password: ")

	if username in users and users[username]["password"] == password:
		print(f"Login successful. Welcome, {users[username]['role']}!")
		return users[username]["role"]
	else:
		print("Invalid username or password.")
		return None


role = login()

if role:
	if role == "Admin":
		print("You can access all features.")
	elif role == "Customer":
		print("You can place orders and view products.")
	elif role == "Cashier":
		print("You can process payments.")

	try:
		subtotal = float(input("Enter subtotal: "))
	except ValueError:
		print("Invalid subtotal. Please enter a number.")
	else:
		couponCode = input("Enter coupon code (or NONE): ")
		location = input("Enter location (Uganda/Kenya/Other): ")
		discountAmount, taxAmount, finalPrice = calculateFinalPrice(subtotal, couponCode, location)
		print(f"Discount applied: {discountAmount:.2f}")
		print(f"Tax added: {taxAmount:.2f}")
		print(f"Final price: {finalPrice:.2f}")
