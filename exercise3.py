class User:
    def __init__(self, first_name, last_name, username, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"User summary: {self.first_name} {self.last_name}, username {self.username}, email {self.email}, age {self.age}, location {self.location}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user1 = User("Lydia", "Nabwami", "lydia_n", "lydia@example.com", 21, "Kampala")
user2 = User("Brian", "Ssekandi", "brian_s", "brian@example.com", 24, "Entebbe")
user3 = User("Amina", "Nanyonga", "amina_n", "amina@example.com", 19, "Jinja")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()

