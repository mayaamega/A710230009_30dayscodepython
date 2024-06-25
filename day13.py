class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

if __name__ == "__main__":
    dog = Dog("Buddy", "Dog")
    cat = Cat("Whiskers", "Cat")
    bird = Bird("Tweety", "Bird")

    print(f"{dog.name} the {dog.species} says {dog.make_sound()}")
    print(f"{cat.name} the {cat.species} says {cat.make_sound()}")
    print(f"{bird.name} the {bird.species} says {bird.make_sound()}")

