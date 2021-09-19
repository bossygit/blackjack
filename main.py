from random import shuffle

def createDeck():
    Deck = []

    for i in range(0,4):
        faceValues = ["A","J","Q","K"]
        for card in range(2,11):
            Deck.append(card)

        for card in faceValues:
            Deck.append(card)
        return Deck
cardDeck = createDeck()
print(cardDeck)
shuffle(cardDeck)
print("Shuffled")
print(cardDeck)
