import random

class Animal:
    def __init__(self, species, name, size, diet, habitat, lifespan, gender):
        self.species = species
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = 0
        self.satiety = 100  
        self.gender = gender

    def is_alive(self):
        return self.age < self.lifespan and self.satiety > 0

    def grow_older(self):
        self.age += 1
        self.satiety -= 9  

    def eat(self):
        self.satiety = min(self.satiety + 2, 100)

    def hunt(self, success):
        if success:
            self.satiety = min(self.satiety + 53, 100)
        else:
            self.satiety = max(self.satiety - 16, 0)

    def reproduce(self, mate):
        if self.gender == mate.gender:
            return []

        if self.habitat == 'water' and self.satiety > 50 and mate.satiety > 50:
            return [Animal(self.species, self.name, self.size, self.diet, self.habitat, self.lifespan, random.choice(['male', 'female'])) for _ in range(10)]
        elif self.habitat == 'air' and self.satiety > 12 and mate.satiety > 12 and self.age > 3 and mate.age > 3:
            return [Animal(self.species, self.name, self.size, self.diet, self.habitat, self.lifespan, random.choice(['male', 'female'])) for _ in range(4)]
        elif self.habitat == 'land' and self.satiety > 20 and mate.satiety > 20 and self.age > 5 and mate.age > 5:
            return [Animal(self.species, self.name, self.size, self.diet, self.habitat, self.lifespan, random.choice(['male', 'female'])) for _ in range(2)]
        return []

class Ecosystem:
    def __init__(self):
        self.animals = []
        self.plant_food = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def time_step(self):
        new_animals = []
        for animal in self.animals:
            if not animal.is_alive():
                self.plant_food += animal.size
                continue
            animal.grow_older()
            if animal.diet == 'herbivore' and self.plant_food > 0:
                animal.eat()
                self.plant_food -= 1
            elif animal.diet == 'carnivore':
                suitable_prey = [a for a in self.animals if a.species != animal.species and a.diet != 'carnivore']
                if suitable_prey:
                    prey = random.choice(suitable_prey)
                    success = random.random() < 0.5
                    if success:
                        animal.hunt(True)
                        self.animals.remove(prey)
                    else:
                        animal.hunt(False)
                else:
                    animal.satiety = max(animal.satiety - 9, 0)
            if animal.satiety < 10:
                self.plant_food += animal.size
                continue
        self.animals = [animal for animal in self.animals if animal.is_alive()] + new_animals

    def print_status(self):
        print(f"Plant food: {self.plant_food}")
        for i, animal in enumerate(self.animals):
            print(f"ID: {i}, Species: {animal.species}, Age: {animal.age}, Satiety: {animal.satiety}, Gender: {animal.gender}")

    def reproduce_animals(self, id1, id2):
        if id1 >= len(self.animals) or id2 >= len(self.animals):
            print("Invalid animal IDs.")
            return
        animal1 = self.animals[id1]
        animal2 = self.animals[id2]
        if animal1.species != animal2.species:
            print("Animals must be of the same species to reproduce.")
            return
        new_animals = animal1.reproduce(animal2)
        self.animals.extend(new_animals)
        print(f"{len(new_animals)} new animals added.")

species = [
    ("Shark", "Shark", 300, "carnivore", "water", 30),
    ("Tuna", "Tuna", 100, "carnivore", "water", 15),
    ("Seagull", "Seagull", 5, "carnivore", "air", 20),
    ("Eagle", "Eagle", 10, "carnivore", "air", 25),
    ("Elephant", "Elephant", 5000, "herbivore", "land", 70),
    ("Rabbit", "Rabbit", 3, "herbivore", "land", 8),
    ("Deer", "Deer", 200, "herbivore", "land", 20),
    ("Wolf", "Wolf", 50, "carnivore", "land", 15),
    ("Dolphin", "Dolphin", 200, "carnivore", "water", 30),
    ("Hawk", "Hawk", 7, "carnivore", "air", 20),
    ("Lion", "Lion", 190, "carnivore", "land", 20),
    ("Zebra", "Zebra", 300, "herbivore", "land", 25),
]

def main():
    ecosystem = Ecosystem()
    for spec in species:
        gender = random.choice(['male', 'female'])
        ecosystem.add_animal(Animal(*spec, gender))
    
    while True:
        print("\nКоманды:")
        print("1. Показать текущее состояние экосистемы")
        print("2. Добавить животное")
        print("3. Увеличить запас растительной пищи")
        print("4. Смоделировать шаг времени")
        print("5. Смоделировать размножение животных")
        print("6. Выйти")
        
        command = input("Введите команду: ")
        
        if command == "1":
            ecosystem.print_status()
        elif command == "2":
            print("Виды животных:")
            for i, spec in enumerate(species):
                print(f"{i + 1}. {spec[0]}")
            choice = int(input("Выберите вид животного: ")) - 1
            gender = input("Введите пол (male/female): ")
            if choice in range(len(species)):
                ecosystem.add_animal(Animal(*species[choice], gender))
        elif command == "3":
            amount = int(input("Введите количество растительной пищи: "))
            ecosystem.increase_plant_food(amount)
        elif command == "4":
            ecosystem.time_step()
        elif command == "5":
            ecosystem.print_status()
            id1 = int(input("Введите ID первой особи для размножения: "))
            id2 = int(input("Введите ID второй особи для размножения: "))
            ecosystem.reproduce_animals(id1, id2)
        elif command == "6":
            break
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()