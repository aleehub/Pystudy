class SweetPotato(object):

    def __init__(self):

        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    def cook(self, time):

        self.cookedLevel += time

        if self.cookedLevel > 8:

            self.cookedString = "烤成灰了"

        elif self.cookedLevel > 5:

            self.cookedString = "烤好了"

        elif self.cookedLevel > 3:

            self.cookedString = "半生不熟"

        else:

            self.cookedString = "生的"

    def __str__(self):
        msg = self.cookedString + " 地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("
            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg = msg + ")"
        return msg

    def addCondiments(self, condiments):
        self.condiments.append(condiments)


mySweetPotato = SweetPotato()
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)

print(mySweetPotato.condiments)

mySweetPotato.cook(9)

print(mySweetPotato.cookedString)
