# This Programm is household-simulation inspired by "The Sims" to practice OOP. 
# Classes & Attributes (constructor!): Person(name, age, gender). Furniture (type, color). Consumable (name, expiration_date) 
# Composition:  house (contains Rooms, Person, Furniture, Consumables). Link Generations (grandparents, parents and children)
# - Inheritance: Extend Person class: Child, Parent, and Grandparent. Be aware of multiple inheritances.
# - Encapsulation, Properties (Getter & Setter):  make the age attribute private and provide a getter and setter.
# - Copy vs. Deepcopy: Use shallow and deep copies with objects.
# - Mutable Default Arguments: Explore the mutable default argument problem and its solution.
# - Reflection: Use reflection to inspect objects at runtime (e.g., list all attributes of a Person). 
# - Serialization: Implement serialization to save and load the state of your household simulation.
# - Modules: In order to keep the code clean and separated (and practice), the family members are in a diferent module
# 
# To Add:
# - Lazy Loading: # Implement lazy loading for a resource-intensive attribute in one of your classes.
# - Duck Typing and (Runtime) Polymorphism: Show examples of duck typing and polymorphism in your simulation.
# - Dunders (__str__, __repr__, __bool__, etc.): Implementin your classes to define their string representation, boolean conversion, etc.
# - Slots: Use __slots__ in a class to explicitly declare allowed attributes and understand its memory benefits.
# - Object Lifetime & Garbage Collector: Experiment with creating and deleting objects, and observe how Python's garbage collector works.
# - Make a usecase where set/get is better than setter/getter

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__is_hungry = True

    @property
    def generation(self):
        return self.__class__.__name__

    @property
    def stats_individual_overview(self):
        subclass = self.__class__.__name__
        print(f"Name: \t{self.__name}\nAge: \t{self.__age}\nGender:\t{self.__gender}\nType:\t{subclass}")

    @staticmethod
    def create(name, age, gender):
        if age >= 60:
            return Grandparent(name, age, gender)
        if 20 <= age < 60:
            return Parent(name, age, gender)
        if age < 20:
            return Child(name, age, gender)

    def hungry(self):
        if self.__is_hungry == True:
            print(f"{self.__name}: I need something to eat")
    
    def eating(self):
        if self.__is_hungry == True:
            self.__is_hungry = False
            print(f"{self.__name}: A full stomache feels better!")

        if self.__is_hungry == False:
            print(f"{self.__name}: I am not hungry right now.")

class Family:
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []
    
    def add_member(self, person):
        self.members.append(person)
    
    def stats_family_overview(self):
        print(f"Family:\t{self.family_name}")
        for member in self.members:
            print(f"Name:\t{self.family_name}\n\
                    First Name:\t{member._Person__name}\n\
                    Age:\t\t{member._Person__age}\n\
                    Gender:\t{member._Person__gender}\n\
                    Type:\t\t{member.generation}")

class Grandparent(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    
    def telling_stories(self):
        print(f"{self.__name}: Once upon a time when I was young...")
        

class Parent(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def feeding_children(self, child):
        if child.extra_hungry:
            child.extra_hungry = False
            print(f"{self._Person__name}: Here is something to eat {child._Person__name}")
            child.is_extra_hungry()

class Child(Person):    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.extra_hungry = True
    
    def is_extra_hungry(self):
        if self.extra_hungry == True:
            print(f"{self._Person__name}: I can't wait until our next meal. Give me food!")
        if self.extra_hungry == False:
            print(f"{self._Person__name}: Ahhh... now I can last some hours till I bother you again.")
        

parent1 = Person.create("John", 36, "male")
parent2 = Person.create("Mary", 38, "female")
child1 = Person.create("Peter", 9, "male")
child2 = Person.create("Paul", 6, "male")
child3 = Person.create("Sue", 3, "male")
grandparent1 = Person.create("Eduardo", 70, "male")
grandparent2 = Person.create("Matilda", 67, "female")

pearson_family = Family("Pearson")
pearson_family.add_member(parent1)
pearson_family.add_member(parent2)
pearson_family.add_member(child1)
pearson_family.add_member(child2)
pearson_family.add_member(child3)
pearson_family.add_member(grandparent1)
pearson_family.add_member(grandparent2)

# pearson_family.stats_family_overview()
parent1.feeding_children(child1)
