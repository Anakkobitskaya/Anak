import random
def create_deck():
    deck = []
    for i in range(2, 11):
        for e in ('C', 'P', 'B', 'X'):
            deck.append(str(i)+e)
    for i in ('V', 'D', 'K', 'T'):
        for e in ('C', 'P', 'B', 'X'):
            deck.append(i+e)
    return deck

def start(deck):
    hand = []
    for i in range(2):
        hand.append(random.choice(deck))
        deck.remove(hand[-1])
    return hand, deck

def nachalo():
    deck = create_deck()
    hand = []
    hand, deck = start(deck)
    
