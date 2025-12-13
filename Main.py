class Owner:

    class Pet:
        def __init__(self, name, kind, mood, hunger):
            self.name = name
            self.kind = kind
            self.__mood = mood # Настроение
            self.__hunger = hunger # голод

        def feed(self):
            if self.__mood < 90:
                self.__mood += 10
            else:
                self.__mood = 100

            if self.__hunger > 10:
                self.__hunger -= 10
            else:
                self.__hunger = 0
            print(f" {self.kind} {self.name}: Настроение - {self.__mood}, Голод - {self.__hunger}")
        def play(self):
            if self.__mood < 90:
                self.__mood += 10
            else:
                self.__mood = 100

            if self.__hunger < 90:
                self.__hunger += 10
            else:
                self.__hunger = 0

            print(f" {self.kind} {self.name}: Настроение - {self.__mood}, Голод - {self.__hunger}")

        def speak(self):
            pass


        def getMood(self):
            return self.__mood

        def getHunger(self):
            return self.__hunger

    class Cat(Pet):
        def __init__(self, name, kind, mood, hunger):
            super().__init__(name, kind, mood, hunger)

        def speak(self):
            print("Мяу! Мяу!")

    class Dog(Pet):
        def __init__(self, name, kind, mood, hunger):
            super().__init__(name, kind, mood, hunger)

        def speak(self):
            print("Гав! Гав!")

    class Parrot(Pet):
        def __init__(self, name, kind, mood, hunger):
            super().__init__(name, kind, mood, hunger)

        def speak(self):
            print("Чирик! Чирик!")

    class Dragon(Pet):
        def __init__(self, name, kind, mood, hunger):
            super().__init__(name, kind, mood, hunger)

        def speak(self):
            print("Рррааар! Рррааар!")





    def __init__(self, name, age, pets):
        self.name = name
        self.age = age
        self.pets = pets
    def add_pet(self):
        name = input("Имя животного: ")
        kind = input("Животное: ")
        mood = input("Настроение животного: ")
        hunger = input("Голод животного: ")
        if kind == "Кот":
            self.pets.append(Owner.Cat(name, kind, mood, hunger))
        if kind == "Собака":
            self.pets.append(Owner.Dog(name, kind, mood, hunger))
        if kind == "Попугай":
            self.pets.append(Owner.Parrot(name, kind, mood, hunger))
        if kind == "Дракон":
            self.pets.append(Owner.Dragon(name, kind, mood, hunger))

        print("Питомец добавлен")
    def feed_all(self):
        for pet in self.pets:
            pet.feed()
            print(f" {pet.kind} {pet.name}: Настроение - {pet.getMood()}, Голод - {pet.getHunger()}")
    def play_with_all(self):
        for pet in self.pets:
            pet.play()
            print(f" {pet.kind} {pet.name}: Настроение - {pet.getMood()}, Голод - {pet.getHunger()}")

    def get_info(self):
        for pet in self.pets:
            print(f" {pet.kind} {pet.name}: Настроение - {pet.getMood()}, Голод - {pet.getHunger()}")


Ann = Owner("Аня", 26, [Owner.Cat("Степа", "Кот", 50, 50), Owner.Parrot("Гоша", "Попугай", 39, 47)])
Ilia = Owner("Илья", 19, [Owner.Dog("Джем", "Собака", 79, 19), Owner.Dragon("Беззубик", "Дракон", 99, 99)])


people = [Ann, Ilia]

for person in people:
    print(person.name)
    print()
    print(f" 1 — Покормить всех питомцев хозяина")
    print(f" 2 — Поиграть со всеми питомцами")
    print(f" 3 — Добавить нового питомца")
    print(f" 4 — Показать информацию")
    print(f" 5 — Питомцы говорят!")
    print(f" 0 — Выход")

    n = int(input())
    while n != 0:
        if n == 1:
            person.feed_all()
        if n == 2:
            person.play_with_all()
        if n == 3:
            person.add_pet()
        if n == 4:
            person.get_info()
        if n == 5:
            for pet in person.pets:
                print(f"{pet.kind} {pet.name}")
                pet.speak()
                print()
        n = int(input())
