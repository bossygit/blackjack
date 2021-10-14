from random import shuffle
# Set is a list within {}, unordered unindexed, do not allow duplicate values.
def createDeck():
    Deck = []
    faceValues = ["A", "J", "Q", "K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(card)

        for card in faceValues:
            Deck.append(card)
    return Deck

class Player():
    def __init__(self,hand= [],money= 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money

    def __str__(self):
        currentHand =""

        for card in self.hand:
            currentHand += card + " "
        finalStatus = currentHand + "score : " + str(self.score)

        return finalStatus

    def setScore(self):
        self.score = 0

        faceValueDict = {"A":11,
                         "J":10,
                         "K":10,
                         "Q":10,
                         "2":2,
                         "3":3,
                         "4":4,
                         "5":5,
                         "6":6,
                         "7":7,
                         "8":8,
                         "9":9,
                         "10":10}
        aceCounter = 0

        for card in self.hand:
            self.score += faceValueDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score










