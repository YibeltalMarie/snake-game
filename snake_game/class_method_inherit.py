
class Animals :
    def __init__(self):
        self.number_of_eyes = 2
        self.color = "black"
        self.hair_color = "red"

    def use (self):
        print("animals used for medical and other purpose")

class Fish(Animals):
    def __init__(self):
        super().__init__()

    def use (self):
        super().use()
        print("but we are smarter than animals")
        print("everytime believe un your self")

fish = Fish()
fish.use()