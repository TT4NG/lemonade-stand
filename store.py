class Store:
    def __init__(self):
        self.lemons = 0
        self.sugar = 0
        self.ice = 0
        self.cups = 0

    def storePurchase(self):
        print("")
        print("Current account total is", self.account)
        print("What would you like to buy today?")
        print("1 for lemons at $ .75 ", "  currently ", self.lemons)
        print("2 for sugar at $ 2.50 ", "  currently ", self.sugar)
        print("3 for ice at $4.00 ", "  currently ", self.ice)
        print("4 for cups at $1.50 ", "  currently ", self.cups)
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
            print(self.lemons)
            self.account -= 0.75 * lem
            print(self.account)
            return Store.storePurchase(self)
        except ValueError:
            Store.getlemons(self)

    def getsugar(self):
        try:
            sug = input("how much sugar would you like?")
            sug = int(sug)
            self.sugar += sug
            self.account -= 2.50 * sug
            return Store.storePurchase(self)
        except ValueError:
            Store.getsugar(self)

    def getice(self):
        try:
            i = input("how much ice would you like?")
            i = int(i)
            self.ice += i
            self.account -= 4.00 * i
            return Store.storePurchase(self)
        except ValueError:
            Store.getice(self)

    def getcups(self):
        try:
            c = input("how many cups would you like to buy (increments of 20)?")
            c = int(c)
            self.cups += c*20
            self.account -= 1.50 * c
            return Store.storePurchase(self)
        except ValueError:
            Store.getcups(self)