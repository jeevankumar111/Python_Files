class Animal:
    def __init__(self,habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("kennal")

    def sound(self):
        print("Woof Woof!")

x = Dog()
x.print_habitat()
x.sound()