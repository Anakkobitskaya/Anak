import random
def coloda():
    deck = []
    for i in range(2, 11):
        for e in ('C', 'P', 'B', 'X'):
            deck.append(str(i)+e)
    for i in ('J', 'Q', 'K', 'T'):
        for e in ('C', 'P', 'B', 'X'):
            deck.append(i+e)
    return deck

def start(deck):
    hand = []
    for i in range(2):
        hand.append(random.choice(deck)) #Вставка элемента random.choice(desk) в конец списка hand
        deck.remove(hand[-1])            #Удаление последнего элемента из списка desk
    return hand, deck

def nachalo():
    deck = coloda()
    hand = []
    hand, deck = start(deck)
    while True:
        print_hand(hand)
        print_score(hand)
        vopros(hand, deck)

def give_new_kart(deck):
    new_kart = random.choice(deck)
    deck.remove(new_kart)
    return new_kart, deck

def vopros(hand, deck):
    a = input('Хотите взять еще одну карту? ("yes" or "no"): ')
    if a.lower() == 'no':
        exit()
    elif a.lower() == 'yes':
        f = give_new_kart(deck)
        hand.append(f[0])
        deck = f[1]
    else:
        print('Неверный ввод')
                       
def print_hand(hand):
    for kart in hand:
        print(kart, end=' ')
    print()

def print_score(hand):
    costs = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '1': 10,
        'J': 2,
        'Q': 3,
        'K': 4,
        'T': 11
    }
    score = 0
    for kart in hand:
        score += costs[kart[0]] 
    print(score)
nachalo()





    
