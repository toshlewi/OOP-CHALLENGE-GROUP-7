class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type  # New attribute for pet type
        self.hunger = 5  # Starting at midpoint
        self.energy = 5  # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []  # For storing learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍖 {self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"💤 {self.name} took a nap. Energy restored!")

    def play(self):
        if self.energy > 0:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 {self.name} played with you. So fun!")
        else:
            print(f"⚠️ {self.name} is too tired to play. Let them rest!")

    def bath(self):  # New custom action
        self.happiness = min(10, self.happiness + 2)
        print(f"🛁 {self.name} had a bath. They feel fresh and happy!")

    def get_status(self):
        print(f"\n📋 {self.name}'s Status:")
        print(f"Type: {self.pet_type.capitalize()}")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")

    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"🎓 {self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"🤔 {self.name} hasn't learned any tricks yet.")
        else:
            print(f"🤹 {self.name} knows these tricks: {', '.join(self.tricks)}")