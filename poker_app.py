from poker_pkg.player import player_populate, card_exchange, new_hand
from poker_pkg.deck import deck
from poker_pkg.screens import print_table, print_winners
from poker_pkg.validation import player_ck, y_n_ck
from poker_pkg.hand_evaluator import hand_comparision
from poker_pkg.poker_betting import ante, betting_round

card_deck = deck()
pot = {"main_pot": 0, "current_bet": 0}
players = player_populate(player_ck(input("(Max 6) How Many Players 2-6: ")), card_deck)

while True:
    ante(players, pot)

    print_table(players, pot)

    if betting_round(players, pot):
        print_winners(players, pot, hand_comparision(players))
    else:
        card_exchange(players, card_deck)

        betting_round(players, pot)

        print_winners(players, pot, hand_comparision(players))
    
    if y_n_ck(input("Play another hand?\nY/N: ")) == "y":
        card_deck = deck()
        new_hand(players, card_deck)
        continue
    else:
        exit()
    