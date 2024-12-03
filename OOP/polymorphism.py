class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dogs bark")

class Cat(Animal):
    def sound(self):
        print("Cats meow")

# Polymorphic behavior
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()  # Calls the correct version of the sound() method
