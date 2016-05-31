class Store:
    def __init__(self):
        self.lemons = 0
        self.sugar = 0
        self.ice = 0
        self.cups = 0

    def storePurchase(self):
        print("Keep in mind this is Venezuela after the revolution and our goods will be numbered by the day...")
        print("")
        print("Current account total is", self.account)
        print("What would you like to buy today?")
        print("1 for lemons at $", (0.35 * self.days), "  currently ", self.lemons)
        print("2 for sugar at $", (1.50 * self.days), "  currently ", self.sugar)
        print("3 for ice at $", (2.00 * self.days), "  currently ", self.ice)
        print("4 for cups at $", (0.50 * self.days), "  currently ", self.cups)
        print("5 if finished shopping")
        choice = input("enter a selection: ")
        if choice == '1':
            Store.getlemons(self)
        elif choice == '2':
            Store.getsugar(self)
        elif choice == '3':
            Store.getice(self)
        elif choice == '4':
            Store.getcups(self)
        elif choice == '5':
            return
        else:
            print("invalid number")
            return Store.storePurchase(self)

    def getlemons(self):
        try:
            lem = input("how many lemons would you like?")
            lem = int(lem)
            self.lemons += lem
            self.account -= 0.35 * lem * self.days
            if self.account < 0:
                self.account += 0.35 * lem
                print("Not enough cash!")
            return Store.storePurchase(self)
        except ValueError:
            Store.getlemons(self)

    def getsugar(self):
        try:
            sug = input("how much sugar would you like?")
            sug = int(sug)
            self.sugar += sug
            self.account -= 1.50 * sug * self.days
            if self.account < 0:
                self.account += 1.50 * sug * self.days
                print("Not enough cash!")
            return Store.storePurchase(self)
        except ValueError:
            Store.getsugar(self)

    def getice(self):
        try:
            i = input("how much ice would you like?")
            i = int(i)
            self.ice += i
            self.account -= 2.00 * i * self.days
            if self.account < 0:
                self.account += 2.00 * i * self.days
                print("Not enough cash!")
            return Store.storePurchase(self)
        except ValueError:
            Store.getice(self)

    def getcups(self):
        try:
            c = input("how many cups would you like to buy (increments of 20)?")
            c = int(c)
            self.cups += c*20
            self.account -= 0.50 * c * self.days
            if self.account < 0:
                self.account += 0.50 * c * self.days
                print("Not enough cash!")
            return Store.storePurchase(self)
        except ValueError:
            Store.getcups(self)