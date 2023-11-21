# This Programm is household-simulation inspired by "The Sims" to practice OOP. 
# Classes & Attributes (constructor!): Person(name, age, gender). Furniture (type, color). Consumable (name, expiration_date) 
# Composition:  house (contains Rooms, Person, Furniture, Consumables). Link Generations (grandparents, parents and children)
# - Inheritance: Extend Person class: Child, Parent, and Grandparent. Be aware of multiple inheritances.
# - Encapsulation, Properties (Getter & Setter):  make the age attribute private and provide a getter and setter.
# - Copy vs. Deepcopy: Use shallow and deep copies with objects.
# - Mutable Default Arguments: Explore the mutable default argument problem and its solution.
# - Reflection: Use reflection to inspect objects at runtime (e.g., list all attributes of a Person). 
# - Serialization: Implement serialization to save and load the state of your household simulation.
# 
# To Add:
# - Lazy Loading: # Implement lazy loading for a resource-intensive attribute in one of your classes.
# - Duck Typing and (Runtime) Polymorphism: Show examples of duck typing and polymorphism in your simulation.
# - Dunders (__str__, __repr__, __bool__, etc.): Implementin your classes to define their string representation, boolean conversion, etc.
# - Slots: Use __slots__ in a class to explicitly declare allowed attributes and understand its memory benefits.
# - Object Lifetime & Garbage Collector: Experiment with creating and deleting objects, and observe how Python's garbage collector works.
# - Make a usecase where set/get is better than setter/getter
# - Does it make sense to use modules for the different base classes?

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

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
            return Grandparents(name, age, gender)
        if 20 <= age < 60:
            return Parents(name, age, gender)
        if age < 20:
            return Children(name, age, gender)

class Family:
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []
    
    def add_member(self, person):
        self.members.append(person)
    
    def stats_family_overview(self):
        print(f"Family:\t{self.family_name}")
        for member in self.members:
            print(f"Name:\t\t{self.family_name}\n\
                  First Name:\t{member._Person__name}\n\
                  Age:\t\t{member._Person__age}\n\
                  Gender:\t\t{member._Person__gender}\n\
                  Type:\t\t{member.generation}")

class Grandparents(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        ...

class Parents(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        ...

class Children(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        ...

person1 = Person.create("John", 36, "male")
person2 = Person.create("Mary", 38, "female")
person3 = Person.create("Peter", 9, "male")
person4 = Person.create("Paul", 6, "male")
person5 = Person.create("Sue", 3, "male")
person6 = Person.create("Eduardo", 70, "male")
person7 = Person.create("Matilda", 67, "female")

pearson_family = Family("Pearson")
pearson_family.add_member(person1)
pearson_family.add_member(person2)
pearson_family.add_member(person3)
pearson_family.add_member(person4)
pearson_family.add_member(person5)
pearson_family.add_member(person6)
pearson_family.add_member(person7)

pearson_family.stats_family_overview()
