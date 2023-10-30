import random
from poker_pkg.hand_evaluator import evaluate_hand
from poker_pkg.validation import int_ck

class Player:
    def __init__(self, name: str = ''):
        self.name = name
        self.dealer = ''
        self.hand = {"cards": str, "npc_cards": str, "unsuited_cards": [], "suit_only_cards": [], 
                     "hand_rank": {"hand_string": str, "hand_value": int, 
                                   "hand_type": {"is_straight": False, "is_flush": False, "is_quads": False,"is_full_house": False,
                                                 "is_trips": False, "is_two_pair": False, "is_pair": False}}}
        self.money = 10000
        self.bet = 0
        self.fold = False
        self.all_in = False

    def money_get(self) -> int:
        return self.money
    
    def money_set(self, amount: int) -> None:
        self.money = amount

    def fold_get(self) -> bool:
        return self.fold
    
    def fold_set(self) -> None:
        self.fold = True
        self.hand["npc_cards"] = self.hand["cards"] = "Fold"
        self.hand["hand_rank"]["hand_value"] = 0
        self.hand["hand_rank"]["hand_string"] = ""

    def bet_get(self) -> int:
        return self.bet
    
    def bet_set(self, bet: int) -> None:
        self.bet = bet

    def cards_get(self) -> str:
        return self.hand["cards"]
    
    def cards_set(self, hand: str) -> None:
        self.hand["cards"] = ' '.join(hand)

    def unsuited_cards_get(self) -> list:
        return self.hand["unsuited_cards"]
    
    def unsuited_cards_set(self, unsuited_hand: list) -> None:
        self.hand["unsuited_cards"] = unsuited_hand

    def suited_cards_get(self) -> list:
        return self.hand["suit_only_cards"]
    
    def suited_cards_set(self, suited_hand: list) -> None:
        self.hand["suit_only_cards"] = suited_hand

    def npc_cards_get(self) -> str:
        return self.hand["npc_cards"]
    
    def npc_cards_set(self, hand: str) -> None:
        self.hand["npc_cards"] = hand

    def is_straight_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_straight"] = boolen

    def is_straight_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_straight"]
    
    def is_flush_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_flush"] = boolen

    def is_flush_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_flush"]
    
    def is_quads_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_quads"] = boolen

    def is_quads_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_quads"]

    def is_full_house_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_full_house"] = boolen

    def is_full_house_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_full_house"]

    def is_trips_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_trips"] = boolen

    def is_trips_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_trips"]

    def is_two_pair_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_two_pair"] = boolen

    def is_two_pair_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_two_pair"]
    
    def is_pair_set(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_pair"] = boolen

    def is_pair_get(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_pair"]

    def hand_string_set(self, string: str) -> None:
        self.hand["hand_rank"]["hand_string"] = string

    def hand_string_get(self) -> str:
        return self.hand["hand_rank"]["hand_string"]
    
    def hand_value_set(self, value: int) -> None:
        self.hand["hand_rank"]["hand_value"] = value

    def hand_value_get(self) -> int:
        return self.hand["hand_rank"]["hand_value"]

    def hand_reset(self) -> None:
        for item in self.hand["hand_rank"]["hand_type"]:
            self.hand["hand_rank"]["hand_type"][item] = False
        self.hand["hand_rank"]["hand_value"] = 0
        self.hand["hand_rank"]["hand_string"] = ''
        self.hand["cards"] = ''
        self.hand["npc_cards"] = ''
        self.hand["unsuited_cards"].clear()
        self.hand["suit_only_cards"].clear()
        self.bet = 0
        self.fold = False
        self.all_in = False

def player_populate(number_of_players: int, deck: list) -> dict:
    players = {}

    for i in range(6):
        name = f"Player {i + 1}" 
        hand =[]
        
        if i < number_of_players:    
            
            for x in range(5):
                hand.append(deck.pop())  

            players[name] = Player(name)
            players[name].cards_set(hand)

            hand_translator(players[name])

            evaluate_hand(players[name])

            if i == number_of_players - 1:
                players[random.choice(list(players.keys()))].dealer = "D"

        else:
            break

    return players

def card_exchange(players: dict, deck: list) -> None:
    for player in players:
        if not players[player].fold_get():
            hand = players[player].cards_get().split(' ')
            temp_hand = hand.copy()
            unsuited_hand = players[player].unsuited_cards_get()
            discard_list = []
            
            if 14 in unsuited_hand:
                max_discard = 4
            else:
                max_discard = 3

            if players[player].name == "Player 1":
                print(("{:<3} {:<3} {:<3} {:<3} {:<3}".format(1, 2, 3, 4, 5)))
                print ("{:<4} {:<4} {:<4} {:<4} {:<4}".format(hand[0], hand[1], hand[2], hand[3], hand[4]))

                num_cards_to_discard = int_ck(input(f"How many cards will you discard?\n(Max of {max_discard}): ")) 

                while num_cards_to_discard > max_discard: 
                    num_cards_to_discard = int_ck(input(f"You can only discard upto {max_discard} \n(Max of {max_discard}): ")) 
                
                for i in range(num_cards_to_discard):
                    card_index = int_ck(input("Pick card 1-5: "))
                    
                    if card_index >= 1 and card_index <= 5 and card_index not in discard_list:
                        discard_list.append(card_index)
                    else:
                        while card_index < 1 or card_index > 5 or card_index in discard_list:
                            card_index = int_ck(input("Card selection must be 1-5\nand must not be a previously discarded card\nNew card selection: "))
                        discard_list.append(card_index)

                for i in discard_list:
                    hand.pop(hand.index(temp_hand[i - 1]))

            else:
                hand_value = players[player].hand_value_get()
                player_unsuited_occurance = list(set([x for i,x in enumerate(unsuited_hand) if unsuited_hand.count(x) > 1]))
                player_temp_hand = list(filter(lambda i: i not in player_unsuited_occurance, unsuited_hand))
                
                if hand_value >= 5:
                    continue
                else:
                    count = 0
                    for card in sorted(player_temp_hand):
                        if card < 10 and count <= max_discard:
                            hand.pop(hand.index(temp_hand[unsuited_hand.index(card)]))
                            count += 1
                        
            for i in range(5 - len(hand)):
                hand.append(deck.pop())
            
            players[player].cards_set(hand)

            hand_translator(players[player])

            evaluate_hand(players[player])

def hand_translator(player: Player) -> None:
    player_cards = player.cards_get().split(" ")
    player_hand_unsuited = player.unsuited_cards_get()
    player_hand_suited = player.suited_cards_get()

    player_hand_unsuited.clear()
    player_hand_suited.clear()

    for card in player_cards:
        value = card[:len(card)-2]
        player_hand_suited.append(card[len(card)-2:])

        if value == "A":
            player_hand_unsuited.append(14)
        elif value == "K":
            player_hand_unsuited.append(13)
        elif value == "Q":
            player_hand_unsuited.append(12)
        elif value == "J":
            player_hand_unsuited.append(11)
        else:
            player_hand_unsuited.append(int(value))

    if player.name == "Player 1":
        player.npc_cards_set(player_cards)
    else: 
        player.npc_cards_set("█ █ █ █ █")

def new_hand(players: dict, deck: list) -> None:
    dealer_position = 0

    for player in players:
        if players[player].dealer == "D":
            dealer_position = int(players[player].name[len(players[player].name) - 1:])
            players[player].dealer = ""
            break

    for player in players:
        players[player].hand_reset()

        if players[player].money_get() > 0:
            hand = []
            players[player].hand_reset()
            
            for i in range(5):
                hand.append(deck.pop())

            players[player].cards_set(hand)

            hand_translator(players[player])

            evaluate_hand(players[player])
        else:
            if players[player].name == "Player 1":
                print("GAME OVER")
                exit()
            else:
                players.pop(players[player].name)

    
    if dealer_position + 1 > len(players):
        players["Player 1"].dealer = "D"
    else:
        players[f"Player {dealer_position +1 }"].dealer = "D"
    
    if len(players) == 1:
        print("YOU WIN")
