countries = ["Canada", "Mexico", "USA", "Brazil", "Argentina", "France", "England"]
winner = "Canada"

print("Countries taking part in the World Cup game:")
print(", ".join(countries))

while True:
	guess = input("Type a country that will win World Cup 2026, or type 'quit': ").strip().lower()

	if guess == "":
		print("Please enter a country name.")
		continue

	if guess == "pass":
		pass
		print("You chose to pass.")
	elif guess not in [country.lower() for country in countries]:
		print("That country is not in the list.")
	elif guess == winner.lower():
		print("Canada will win World Cup 2026!")
		break
	elif guess == "quit":
		print("Game ended.")
		break
	else:
		print("Not the winner. Try again.")

