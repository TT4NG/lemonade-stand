
class Types:
    def __init__(self):
        self.thirst = 0

    def old(self):
        self.thirst = 2
        if weather == 1:
            self.thirst += 2
        elif weather == 2:
            self.thirst += 0
        elif weather == 3:
            self.thirst += 1

    def normal(self):
        self.thirst = 4
        if weather == 1:
            self.thirst += 2
        elif weather == 2:
            self.thirst += 0
        elif weather == 3:
            self.thirst += 1

    def jogger(self):
        self.thirst = 6
        if weather == 1:
            self.thirst += 2
        elif weather == 2:
            self.thirst += 0
        elif weather == 3:
            self.thirst += 1
