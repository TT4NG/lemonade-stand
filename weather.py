import random


class Weather:
    def __init__(self):
        self.weather = 0

    def weathertype(self):
        choice = random.randrange(1, 4)
        if choice == 1:
            print("Hot and Sunny")
        elif choice == 2:
            print("Cloudy and Windy")
        elif choice == 3:
            print("Rainy and Muggy")
        self.weather = choice
