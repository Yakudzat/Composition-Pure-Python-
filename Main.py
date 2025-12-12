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



