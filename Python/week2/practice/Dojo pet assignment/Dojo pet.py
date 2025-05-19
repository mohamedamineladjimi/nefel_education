class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()

    def feed(self):
        if self.pet_food > 0:
            print(f"{self.first_name} feeds {self.pet.name}.")
            self.pet.eat()
            self.pet_food -= 1
        else:
            print("No more pet food!")

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping. Energy increased to {self.energy}.")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy: {self.energy}, Health: {self.health}.")

    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health increased to {self.health}.")

    def noise(self):
        print(f"{self.name} makes a happy sound!")
buddy = Pet(name="Buddy", type="Dog", tricks=["sit", "roll over"])

ninja_ken = Ninja(first_name="Ken", last_name="Yamada", treats=5, pet_food=3, pet=buddy)

ninja_ken.walk()
ninja_ken.feed()
ninja_ken.bathe()