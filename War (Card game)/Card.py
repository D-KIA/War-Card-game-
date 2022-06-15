# suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
# ranks: (1,2,3,4,5,6,7,8,9,10,11,12,13)
# Each suit includes three court cards (face cards), King, Queen and Jack, with reversible (double-headed) images
# Each suit also includes ten numeral cards or pip cards, from one to ten.
'''   if p1_card.rank == p2_card.rank:
        print('War !!!!')
        if len(player1.holding) < 5:
            print("player 1 can't play war so player 2 win" )
            break
        elif len(player2.holding) < 5:
            print("player 2 can't play war so player 1 win" )
            break
        for l in range(1, 6):
            war1.append(player1.remove())
            war2.append(player2.remove())
        p1_card = player1.remove()
        p2_card = player2.remove()
        if p1_card == p2_card:
            print('Tie')
            player1.add_card(war1)
            player2.add_card(war2)
            continue '''

import random
suit = ['clubs', 'diamonds', 'hearts', 'spades']

rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
         'Queen': 12, 'King': 13, 'Ace': 14}

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class deck():
    def __init__(self):
        self.all_cards = []
        for item in suit:
            for num in rank:
                self.all_cards.append(card(item, num))
    def shuffel(self):
        random.shuffle(self.all_cards)
    def deal(self):
        return self.all_cards.pop(0)

class player:
    def __init__(self, name):
        self.name = name
        self.holding = []
    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.holding.extend(new_cards)
        else:
            self.holding.append(new_cards)
    def remove(self):
        return self.holding.pop(0)
    def __str__(self):
        return f' {self.name} is holding {len(self.holding)} cards'

player1 = player('One')
player2 = player('Two')

cdeck = deck()
cdeck.shuffel()
for n in range(1, 53):
    if n % 2 == 0:
        player1.add_card(cdeck.deal())
    else:
        player2.add_card(cdeck.deal())
n = 0
while len(player1.holding) != 0 and len(player2.holding) != 0:
    n = n+1
    print(f'round {n}')
    war1 = []
    war2 = []
    p1_card = player1.remove()
    p2_card = player2.remove()
    while p1_card.value == p2_card.value:
        print('WAR !!!')
        if len(player1.holding) >= 6 and len(player2.holding) >= 6:
            for l in range(1, 6):
                war1.append(player1.remove())
                war2.append(player2.remove())
        else:
            if len(player1.holding) > len(player2.holding):
                print("Player 1 wins as player 2 can't play the war")
                exit()
            else:
                print("Player 2 wins as player 1 can't play the war")
                exit()
        p1_card = player1.remove()
        p2_card = player2.remove()
    if p1_card.value > p2_card.value:
        print('Player 1 won this round')
        player1.add_card(war1)
        player1.add_card(war2)
        player1.add_card(p1_card)
        player1.add_card(p2_card)
    else:
        print('Player 2 won this round')
        player2.add_card(war1)
        player2.add_card(war2)
        player2.add_card(p1_card)
        player2.add_card(p2_card)
if len(player2.holding) == 0:
    print('Player 1 Is The Winner')
else:
    print('Player 2 Is The Winner')







