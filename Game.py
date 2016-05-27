from bankroll import Bankroll
from weather import Weather
from Player import Player
from store import Store
from Recipe import Recipe
from customers import Customers


class Game:
    def __init__(self):
        self.player1 = None
        self.playerhigh = None
        self.lemons = 0
        self.sugar = 0
        self.ice = 0
        self.cups = 0
        self.account = None
        self.pitcher = 0
        self.price = 0
        self.weather = 0
        self.customers = 0
        self.normal = 0
        self.old = 0
        self.jogger = 0
        self.thirst = 0
        self.day = 0
        self.days = 1
        self.increase = float(0)
        self.thirstold = 6
        self.thirstnorm = 5
        self.thirstjogger = 3
        self.highscore = 0


    def startText(self):
        self.day = 0
        print("Welcome to Lemonade Stand!")
        print("The game is simple, test various lemonade recipes while staying within budget and try to make a profit")
        self.daycounter()
        print("You have a total of ", self.day, " days to make as much profit as you can, best of Luck")
        self.cash()
        self.player1 = self.getplayer()
        print(self.player1.name, "your mother has given you", self.account, "for the summer good luck on your stand")
        self.nextText()

    def nextText(self):
        print("")
        print("Day's left: ", self.day)
        print("current High Score is ", self.highscore, "held by ", self.playerhigh)
        while self.day > 0 and self.account > 0:

            self.grabstore()
            print("")

            self.Inventory()
            print("")

            self.recipesjump(self.lemons, self.sugar, self.ice)

            self.customer()

            self.grabweather()

            self.setprice()

            self.purchase()

            self.day -= 1
            self.days += 1
            self.ice = 0

            self.nextText()
        while self.day == 0 or self.account == 0:
            print("game over", self.account)
            self.restart()



    def getplayer(self):
        name = input("Please enter your name: ")
        player = Player(name)
        return player

    def grabweather(self):
        print("Today's forecast is ")
        weather = Weather()
        weather.weathertype()
        self.weather = weather.weather

    def cash(self):
        Bankroll.AccountInitial(self)

    def grabstore(self):
        print("Now lets buy some ingredients")
        print("Take note that ice will melt by the end of day but other ingredients will remain")
        Store.storePurchase(self)

    def Inventory(self):
        print("lemons = ", self.lemons)
        print("sugar = ", self.sugar)
        print("ice = ", self.ice)
        print("cups = ", self.cups)

    def recipesjump(self, lemons, sugar, ice):
        recip = Recipe()
        recip.recipes(lemons, sugar, ice)
        self.pitcher = recip.pitcher
        self.lemons -= recip.lemonus
        self.sugar -= recip.sugaruse
        self.ice -= recip.iceuse


    def customer(self):
        custom = Customers()
        custom.passers()
        self.old = custom.old
        self.normal = custom.normal
        self.jogger = custom.jogger
        self.customers = custom.custom

    def setprice(self):
        print("how much would you like to sell at?")
        price = input()
        try:
            self.price = float(price)
            if self.price > 0:
                if self.price <= 0.25:
                    self.thirst -= 1
                elif self.price > 0.75 and  self.price <= 1.50:
                    print("thats a bit high but ok")
                    self.thirst += 1
                elif self.price > 1.50 and self.price <= 2.00:
                    print("good luck selling that high")
                    self.thirst += 2
                elif self.price <= 0.75 and self.price > 0.25:
                    print("thats an alright price")
                    self.thirst += 0
                else:
                    print("Their thirst would have to be over NINE THOUSAND to buy that")
                    self.thirst += 9000
            else:
                print("We're running a business nothing's free!!")
                Game.setprice(self)
        except ValueError:
            print("invalid price")
            Game.setprice(self)

    def purchase(self):
        self.increase1 = 0
        self.increase2 = 0
        self.increase3 = 0
        if self.weather == 1:
            self.thirst -= 1
        elif self.weather == 2:
            self.thirst += 0
        elif self.weather == 3:
            self.thirst += 1
        self.thirsto = self.thirst + self.thirstold
        self.thirstno = self.thirst + self.thirstnorm
        self.thirstj = self.thirst + self.thirstjogger
        while self.old != 0 and self.cups != 0:
            if self.thirsto <= self.pitcher:
                self.cups -= 1
                self.old -= 1
                self.increase1 += self.price
            else:
                break
        while self.normal != 0 and self.cups != 0:
            if self.thirstno <= self.pitcher:
                self.cups -= 1
                self.normal -= 1
                self.increase2 += self.price
            else:
                break
        while self.jogger != 0 and self.cups != 0:
            if self.thirstj <= self.pitcher:
                self.cups -= 1
                self.jogger -= 1
                self.increase3 += self.price
            else:
                break
        self.account += self.increase1 + self.increase2 + self.increase3
        print("you made: ", self.increase1 + self.increase2 + self.increase3)
        print("On to the next day!")
        self.thirst = 0

    def daycounter(self):
        print("As the amount of time progresses goods will become more expensive to purchase")
        print("how many days would you like to play for: ")
        print("1 play for 3 days")
        print("2 play for 5 days")
        print("3 play for 7 days")
        d = input("choose an option: ")
        print("")
        try:
            day = int(d)
            if day == 1:
                self.day = 3
            elif day == 2:
                self.day = 5
            elif day == 3:
                self.day = 7
        except ValueError:
            print("invalid choice")
            print("")
            self.daycounter()

    def restart(self):
        while self.account > self.highscore:
            print("new high score")
            self.highscore = self.account
            self.playerhigh = self.player1.name

        answer = input("would you like to play again? Y/N: ")
        print(answer)
        if answer.lower() == "y":
            self.startText()
        elif answer.lower() == "n":
            print("Goodbye.")
        else:
            print("Invalid, type Y or N")
            self.restart()