# creates parent class which is animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " eats food.")

    def make_sound(self):
        print(self.name + " makes a sound.")


# creates child class which is lion
class Lion(Animal):
    def make_sound(self):
        print(self.name + " roars loudly!")

    def eat(self):
        print(self.name + " eats fresh meat.")


# creates another child class called elephant
class Elephant(Animal):
    def make_sound(self):
        print(self.name + " trumpets!")

    def eat(self):
        print(self.name + " eats grass and fruits.")


# creates another child class called monkey
class Monkey(Animal):
    def make_sound(self):
        print(self.name + " chatters!")

    def eat(self):
        print(self.name + " eats bananas.")


# creates objects
simba = Lion("Simba")
dumbo = Elephant("Dumbo")
george = Monkey("George")

# puts in a list and call the objects using a for loop
animals = [simba, dumbo, george]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
