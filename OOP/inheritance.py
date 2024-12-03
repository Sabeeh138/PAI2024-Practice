# 1. Single Inheritance: One child class inherits from one parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):  # Single inheritance
    def sound(self):
        print("Dogs bark")

dog = Dog()
dog.sound()  # Output: Dogs bark

# 2. Multilevel Inheritance: A class inherits from another class, which inherits from another
class Mammal(Animal):
    def characteristic(self):
        print("Mammals give live birth")

class Human(Mammal):  # Multilevel inheritance
    def language(self):
        print("Humans can speak")

human = Human()
human.sound()          # Inherited from Animal
human.characteristic()  # Inherited from Mammal
human.language()        # Defined in Human

# 3. Multiple Inheritance: A class inherits from more than one parent class
class Bird:
    def fly(self):
        print("Birds can fly")

class Bat(Mammal, Bird):  # Multiple inheritance
    def nocturnal(self):
        print("Bats are nocturnal")

bat = Bat()
bat.fly()            # Inherited from Bird
bat.characteristic()  # Inherited from Mammal
bat.nocturnal()       # Defined in Bat

# 4. Hierarchical Inheritance: Multiple child classes inherit from one parent class
class Cat(Animal):  # Hierarchical inheritance
    def sound(self):
        print("Cats meow")

cat = Cat()
cat.sound()  # Output: Cats meow

# 5. Hybrid Inheritance: Combines two or more types of inheritance
class AquaticAnimal:
    def habitat(self):
        print("Aquatic animals live in water")

class Amphibian(Mammal, AquaticAnimal):  # Hybrid inheritance
    def unique(self):
        print("Amphibians can live both on land and in water")

amphibian = Amphibian()
amphibian.characteristic()  # From Mammal
amphibian.habitat()         # From AquaticAnimal
amphibian.unique()          # Defined in Amphibian
