class Recipe:
    def __init__(self, ):
        self.pitcher = 0
        self.sugaruse = 0
        self.iceuse = 0
        self.lemonus = 0



    def recipes(self, lemons, sugar, ice):
        print("Lets try out our recipes today")
        Recipe.le(self, lemons)
        Recipe.sugs(self, sugar)
        Recipe.ic(self, ice)
        print("")
        print("time to make the pitcher")

        if self.sugaruse == self.lemonus and self.sugaruse > 0 and self.lemonus >0:
            Recipe.halfnhalf(self)

        elif self.sugaruse > self.lemonus and self.lemonus > 0 and self.iceuse == 0:
            Recipe.sugarylemonade(self)

        elif self.sugaruse > self.lemonus and self.lemonus == 0:
            Recipe.sugarwater(self)

        elif self.sugaruse == 0 and self.lemonus > self.sugaruse:
            Recipe.wholelemons(self)

        elif self.sugaruse > 0 and self.lemonus > self.sugaruse:
            Recipe.tartlemonade(self)

        elif self.sugaruse > self.lemonus and self.lemonus > 0 and self.iceuse > 0:
            Recipe.perfectMIX(self)

        else:
            Recipe.shit(self)

    def le(self, lemons):
        print("current lemons = ", lemons)
        lem = input("how many many lemons would you like to use?")
        print("")
        try:
            self.lemonus = int(lem)
            if self.lemonus >= 0 and self.lemonus <= lemons:
                lemons -= self.lemonus
            else:
                print("invalid number")
                Recipe.le(self, lemons)
        except ValueError:
            print("invalid use")
            Recipe.le(self, lemons)

    def sugs(self, sugar):
        print("current sugar = ", sugar)
        sug = input("how much sugar should we use to make it sweet?")
        print("")
        try:
            self.sugaruse = int(sug)
            if self.sugaruse >= 0 and self.sugaruse <= sugar:
                sugar -= self.sugaruse
            else:
                print("invalid number")
                Recipe.sugs(self, sugar)
        except ValueError:
            print("invalid number")
            Recipe.sugs(self, sugar)

    def ic(self, ice):
        print("current ice = ", ice)
        i = input("how much ice should use for the pitcher?")
        print("")
        try:
            self.iceuse = int(i)
            if self.iceuse >= 0 and self.iceuse <= ice:
                ice -= self.iceuse
            else:
                print("invalid number")
                Recipe.ic(self, ice)
        except ValueError:
            print("invalid number")
            Recipe.ic(self, ice)

    def halfnhalf(self):
        print("alright we've made our pitcher Half n Half")
        self.pitcher = 7

    def sugarylemonade(self):
        print("alright we've made our pitcher Sweet")
        self.pitcher = 5

    def tartlemonade(self):
        print("alright we've made our pitcher Tart")
        self.pitcher = 4

    def sugarwater(self):
        print("alright we've made our pitcher of sugar water...great job")
        self.pitcher = 4

    def wholelemons(self):
        print("alright we've made our pitcher of WHOLE LEMONS, are you even trying")
        self.pitcher = 2

    def perfectMIX(self):
        print("alright we've made our pitcher a perfect mix, everyone's gonna want this shit")
        self.pitcher = 7

    def shit(self):
        print("u didnt even try")
        self.pitcher = 0
