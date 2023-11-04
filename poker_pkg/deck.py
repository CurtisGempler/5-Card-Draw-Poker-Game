import random

def deck():
    card_deck = []
    for suit in ["♦️","♣️","♥️","♠️"]:
        for rank in range(2, 15):
            if rank <= 10:
                card_deck.append(f"{rank}{suit}")
            elif rank == 11:
                card_deck.append(f"J{suit}")
            elif rank == 12:
                card_deck.append(f"Q{suit}")
            elif rank == 13:
                card_deck.append(f"K{suit}")
            elif rank == 14:
                card_deck.append(f"A{suit}")

    random.shuffle(card_deck)

    return card_deck
