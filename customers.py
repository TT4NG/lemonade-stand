import random

class Customers:
    def __init__(self):
        self.custom = 0
        self.old = 0
        self.normal = 0
        self.jogger = 0

    def passers(self):
        print("lets see the spread of customers today")
        self.custom = random.randint(25, 50)

        if self.custom >= 25 and self.custom <= 30:
            print("standard", self.custom)

            Customers.standard(self)

        elif self.custom > 30 and self.custom <= 40:
            print("irregular", self.custom)
            Customers.irregular(self)

        else:
            print("ALOT", self.custom)
            Customers.Max(self)

    def standard(self):
        self.old = 5
        self.normal = 20
        self.jogger = self.custom - (self.old + self.normal)
        print("old: ", self.old, "normal: ", self.normal, "joggers: ", self.jogger)

    def irregular(self):
        self.old = 5
        self.normal = 25
        self.jogger = self.custom - (self.old + self.normal)
        print("old: ", self.old, "normal: ", self.normal, "joggers: ", self.jogger)

    def Max(self):
        self.old = 8
        self.normal = 26
        self.jogger = self.custom - (self.old + self.normal)
        print("old: ", self.old, "normal: ", self.normal, "joggers: ", self.jogger)
