class Owner:

    class Pet:
        def __init__(self, name, kind, mood, hunger):
            self.name = name
            self.kind = kind
            self.__mood = mood # Настроение
            self.__hunger = hunger # голод

        def feed(self):
            self.__mood += 10
            self.__hunger -= 10

        def play(self):
            self.__mood += 10
            self.__hunger += 10

        def speak(self):
            return ""

    def __init__(self, name, age, pets):
        self.name = name
        self.age = age
        self.pets = pets
    def add_pet(self, pets):
        self.pets.append(Owner.Pet)

    def feed_all(self):
        for pet in self.pets:
            pet.feed()

    def play_with_all(self):
        for pet in self.pets:
            pet.play()

    def get_info(self):
        for pet in self.pets:
            print(f" {pet.kind} {pet.name}: Настроение - {pet.mood}, Голод - {pet.hunger}")








































