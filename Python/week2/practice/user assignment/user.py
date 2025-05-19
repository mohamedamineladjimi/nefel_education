class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a rewards member.")

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points to spend.")
user1 = User("Jane", "Doe", "jane.doe@example.com", 30)
user1.display_info()
user1.enroll()
user1.spend_points(50)
user1.display_info()
