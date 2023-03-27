# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:17:02 2022

@author: villi
"""

import os.path

class Pet:
    def init(self, name, hunger=0, affection=0):
        self.name = name
        self.hunger = hunger
        self.affection = affection

    def __str__(self):
        return f"{self.name}, Hunger: {self.hunger}, Affection: {self.affection}"

    def __lt__(self, other):
        return self.name < other.name

    def pet(self):
        self.affection += 1
        print(f"You pet {self.name}.")

    def feed(self):
        self.hunger -= 1
        print(f"You feed {self.name}.")
        
def load_pets_from_file(file_path):
    pets = []
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for line in file:
                pet_info = line.strip().split(",")
                pet = Pet(pet_info[0], int(pet_info[1]), int(pet_info[2]))
                pets.append(pet)
    else:
        print("Error: File not found.")
    return pets

def save_pets_to_file(file_path, pets):
    with open(file_path, "w") as file:
        for pet in pets:
            file.write(f"{pet.name},{pet.hunger},{pet.affection}\n")
def list_pets(pets):
    if not pets:
        print("No pets found.")
    else:
        for i, pet in enumerate(pets):
            print(f"{i+1}. {pet}")
def find_pet(pets, name):
    for pet in pets:
        if pet.name.lower() == name.lower():
            return pet
    return None

def main():
    file_path = "pets.txt"
    pets = load_pets_from_file(file_path)

    while True:
        print("\nWelcome to PetRobo! What can I assist you with?")
        print("1. List pets and their status")
        print("2. Find pet")
        print("3. Pet pet")
        print("4. Feed pet")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            list_pets(pets)
        elif choice == "2":
            name = input("Which pet do you want me to find? ")
            pet = find_pet(pets, name)
            if pet:
                print(f"Found {pet.name} under the couch.")
                while True:
                    print("What should I do now?")
                    print("1. Pet pet")
                    print("2. Feed pet")
                    print("3. Back to main menu")
                    sub_choice = input("> ")
                    if sub_choice == "1":
                        pet.pet()
                    elif sub_choice == "2":
                        pet.feed()
                    elif sub_choice == "3":
                        break
                    else:
                        print("Invalid choice.")
            else:
                print(f"Sorry, I could not find {name}.")
        elif choice == "3":
            name = input("Which pet do you want me to pet? ")
            pet = find_pet(pets, name)
            if pet:
                pet.pet()
            else:
                print(f"Sorry, I could not find {name}.")
        elif choice == "4":
            name = input("Which pet do you want me to feed? ")
            pet = find_pet(pets, name)
            if pet:
                pet.feed()
            else:
                print(f"Sorry, I could not find {name}.")
        elif choice == "5":
            save_pets_to_file(file_path, pets)
            print("Program terminated. Thank you for using PetRobo!")
        else:
            print("Invalid choice, please try again.\n")

main()