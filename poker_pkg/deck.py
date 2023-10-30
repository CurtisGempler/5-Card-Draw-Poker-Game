import random

def deck():
    card_deck = []
    for i in range(13):
        if i + 2 <= 10:
            card_deck.append(f"{i + 2}♦️")
            card_deck.append(f"{i + 2}♣️")
            card_deck.append(f"{i + 2}♥️")
            card_deck.append(f"{i + 2}♠️")
        elif i + 2 == 11:
            card_deck.append("J♦️")
            card_deck.append("J♣️")
            card_deck.append("J♥️")
            card_deck.append("J♠️")
        elif i + 2 == 12:
            card_deck.append("Q♦️")
            card_deck.append("Q♣️")
            card_deck.append("Q♥️")
            card_deck.append("Q♠️")
        elif i + 2 == 13:
            card_deck.append("K♦️")
            card_deck.append("K♣️")
            card_deck.append("K♥️")
            card_deck.append("K♠️")
        elif i + 2 == 14:
            card_deck.append("A♦️")
            card_deck.append("A♣️")
            card_deck.append("A♥️")
            card_deck.append("A♠️")
    
    random.shuffle(card_deck)
    
    return card_deck
