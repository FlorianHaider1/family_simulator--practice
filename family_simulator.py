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
import tkinter as tk
import sound_player
import threading

player = sound_player.Player() 

def soundtrack(song, times):
    song_selected = False
    if song == "katyusha":
        song_selected = sound_player.Song(sound_player.Song_collection.katyusha, 120)
    elif song == "korobeiniki":
        song_selected = sound_player.Song(sound_player.Song_collection.korobeiniki, 120)
    elif song == "the_shire":
        song_selected = sound_player.Song(sound_player.Song_collection.the_shire, 90)
    elif song == "war_ensemble":
        song_selected = sound_player.Song(sound_player.Song_collection.war_ensemble_intro, 150)

    if song_selected: 
        sound_player.playback(song_selected, times)

def play_song_in_thread(song, times):
    thread = threading.Thread(target=soundtrack, args=(song, times))
    thread.start()

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__is_hungry = True


    def get_name(self):
        return self.__name

    @property
    def generation(self):
        return self.__class__.__name__

    @property
    def stats_individual_overview(self):
        subclass = self.__class__.__name__
        return f"Name: \t{self.__name}\nAge: \t{self.__age}\nGender:\t{self.__gender}\nType:\t{subclass}"

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
            return f"{self.__name}: I need something to eat"
    
    def eating(self):
        if self.__is_hungry == True:
            self.__is_hungry = False
            return f"{self.__name}: A full stomache feels better!"

        if self.__is_hungry == False:
            return f"{self.__name}: I am not hungry right now."

class Family:
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []
    
    def add_member(self, person):
        self.members.append(person)
    
    def stats_family_overview(self):
        return f"Family:\t{self.family_name}"
        for member in self.members:
            return f"Name:\t{self.family_name}\n\
                    First Name:\t{member._Person__name}\n\
                    Age:\t\t{member._Person__age}\n\
                    Gender:\t{member._Person__gender}\n\
                    Type:\t\t{member.generation}"

class Grandparent(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    
    def telling_stories(self, child):
        child.bored = 0
        return f"{self._Person__name}: Once upon a time when I was young..."
        

class Parent(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def feeding_children(self, child):
        if child.extra_hungry:
            child.extra_hungry = False
            return f"{self._Person__name}: Here is something to eat {child._Person__name}"
            child.is_extra_hungry()

class Child(Person):    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.extra_hungry = True
        self.bored = 0
        self.attention = False
    
    def is_extra_hungry(self):
        if self.extra_hungry == True:
            return f"{self._Person__name}: I can't wait until our next meal. Give me food!"
        if self.extra_hungry == False:
            return f"{self._Person__name}: Ahhh... now I can last some hours till I bother you again."
    
    def getting_bored(self):
        self.bored += 10
        if self.bored < 50:
            return f"{self._Person__name}: *is playing alone*"

        if self.bored > 50 and self.bored < 80:
            return f"{self._Person__name}: *starts getting bored*"

        if self.bored >= 80:
            self.attention = True
            return f"{self._Person__name}: Im booooored!! Give me attention!"


fam1_parent1 = Person.create("John", 36, "male")
fam1_parent2 = Person.create("Mary", 38, "female")
fam1_child1 = Person.create("Peter", 9, "male")
fam1_child2 = Person.create("Paul", 6, "male")
fam1_child3 = Person.create("Sue", 3, "male")
fam1_grandparent1 = Person.create("Eduardo", 70, "male")
fam1_grandparent2 = Person.create("Matilda", 67, "female")

pearson_family = Family("Pearson")
pearson_family.add_member(fam1_parent1)
pearson_family.add_member(fam1_parent2)
pearson_family.add_member(fam1_child1)
pearson_family.add_member(fam1_child2)
pearson_family.add_member(fam1_child3)
pearson_family.add_member(fam1_grandparent1)
pearson_family.add_member(fam1_grandparent2)

fam2_parent1 = Person.create("Steve", 32, "male")
fam2_parent2 = Person.create("Cindy", 30, "female")
fam2_child1 = Person.create("Gurt", 9, "male")
fam2_child2 = Person.create("Gundula", 6, "female")
fam2_grandparent1 = Person.create("Rose", 68, "female")

bennett_family = Family("Bennett")
bennett_family.add_member(fam2_parent1)
bennett_family.add_member(fam2_parent2)
bennett_family.add_member(fam2_child1)
bennett_family.add_member(fam2_child2)
bennett_family.add_member(fam2_grandparent1)


def start():
    text = Child.getting_bored(fam1_child1)
    output(text)

def show_person_info(event=None):
    name = name_entry.get()
    for member in pearson_family.members:
        if member.get_name().lower() == name.lower():
            output(f"{member.stats_individual_overview}\n\n")
            return
    output("Person not found\n\n")

def output(text):
    text_output.configure(state="normal")
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, text)
    text_output.configure(state="disabled")
    text_output.see(tk.END)    

def update_instructions(family):
    instructions.configure(state="normal")
    instructions.delete(1.0, tk.END)
    instructions.insert(tk.END, f"{family.family_name} Family\n ")
    for member in family.members:
        instructions.insert(tk.END, f"{member.get_name()}, {member.generation}\n ")
    instructions.configure(state="disabled")
    
def update_family_info():
    selected_family = selected_family_var.get()
    if selected_family == "Pearson":
        update_instructions(pearson_family)
    if selected_family == "Bennett":
        update_instructions(bennett_family)

# GUI
root = tk.Tk()
root.geometry('1024x600')
root.title("Family Simulator")
root.configure(bg = "black")

top_frame = tk.Frame(root)
top_frame.pack(side="top", fill=tk.X)

selected_family_var = tk.StringVar(value="Pearson")
pearson_rb = tk.Radiobutton(top_frame, text="Pearson Family", variable=selected_family_var, value ="Pearson", command=update_family_info)
pearson_rb.pack(side="left", padx = 10)
bennett_rb = tk.Radiobutton(top_frame, text="Bennett Family", variable=selected_family_var, value ="Bennett", command=update_family_info)
bennett_rb.pack(side="left", padx = 10)

play_shire_button = tk.Button(top_frame, text="Play 'The Shire'", command=lambda: play_song_in_thread("the_shire", 1))
play_shire_button.pack(side="right", padx = 10)
play_koro_button = tk.Button(top_frame, text="Play 'Korobeiniki'", command=lambda: play_song_in_thread("korobeiniki", 1))
play_koro_button.pack(side="right", padx = 10)
play_katy_button = tk.Button(top_frame, text="Play 'Katyusha'", command=lambda: play_song_in_thread("katyusha", 1))
play_katy_button.pack(side="right", padx = 10)

instructions = tk.Text(root, height = 20, width = 25)
instructions.pack(side="left", padx=10, pady=10)

actions = tk.Text(root, height=20, width=20)
actions.insert(tk.END, "Actions:\n\nFeed\nEntertain\nCheck")
actions.configure(state="disabled")
actions.pack(side="right", padx=10, pady=10)
                  
name_entry = tk.Entry(root)
name_entry.pack(pady=5)
name_entry.bind("<Return>", show_person_info)

info_button = tk.Button(root, text="Show info for person", command=show_person_info)
info_button.pack(pady=5)

start_button = tk.Button(root, text="Start", bg="white", command=start)
start_button.pack(side="top", pady=10)

text_output = tk.Text(root, height = 100, width = 50)
text_output.pack(pady=10)

def on_close():
    player.audio_terminate()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

update_instructions(pearson_family)

root.mainloop()