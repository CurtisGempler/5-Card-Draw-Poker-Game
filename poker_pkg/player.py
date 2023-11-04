import random
from poker_pkg.hand_evaluator import evaluate_hand
from poker_pkg.validation import int_ck

class Player:
    def __init__(self, name: str = ''):
        self.name = name
        self.dealer = ''
        self.hand = {"cards": str,
                     "npc_cards": str,
                     "unsuited_cards": [],
                     "suit_only_cards": [], 
                     "hand_rank": {
                        "hand_string": str,
                        "hand_value": int,
                        "hand_type": {
                            "is_straight": False,
                            "is_flush": False,
                            "is_quads": False,
                            "is_full_house": False,
                            "is_trips": False,
                            "is_two_pair": False,
                            "is_pair": False
                }
            }
        }
        self.money = 10000
        self.bet = 0
        self.fold = False
        self.all_in = False

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, amount: int) -> None:
        self._money = amount

    @property
    def fold(self) -> bool:
        return self._fold

    @fold.setter
    def fold(self, value) -> None:
        self._fold = value
        if value:
            self.hand["npc_cards"] = self.hand["cards"] = "Fold"
            self.hand["hand_rank"]["hand_value"] = 0
            self.hand["hand_rank"]["hand_string"] = ""

    @property
    def bet(self) -> int:
        return self._bet

    @bet.setter
    def bet(self, bet: int) -> None:
        self._bet = bet

    @property
    def cards(self) -> str:
        return self.hand["cards"]

    @cards.setter
    def cards(self, hand: list) -> None:
        self.hand["cards"] = ' '.join(hand)

    @property
    def unsuited_cards(self) -> list:
        return self.hand["unsuited_cards"]

    @unsuited_cards.setter
    def unsuited_cards(self, unsuited_hand: list) -> None:
        self.hand["unsuited_cards"] = unsuited_hand

    @property
    def suited_cards(self) -> list:
        return self.hand["suit_only_cards"]

    @suited_cards.setter
    def suited_cards(self, suited_hand: list) -> None:
        self.hand["suit_only_cards"] = suited_hand

    @property
    def npc_cards(self) -> str:
        return self.hand["npc_cards"]

    @npc_cards.setter
    def npc_cards(self, hand: str) -> None:
        self.hand["npc_cards"] = hand

    @property
    def is_straight(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_straight"]

    @is_straight.setter
    def is_straight(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_straight"] = boolen

    @property
    def is_flush(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_flush"]

    @is_flush.setter
    def is_flush(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_flush"] = boolen

    @property
    def is_quads(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_quads"]

    @is_quads.setter
    def is_quads(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_quads"] = boolen

    @property
    def is_full_house(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_full_house"]

    @is_full_house.setter
    def is_full_house(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_full_house"] = boolen

    @property
    def is_trips(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_trips"]

    @is_trips.setter
    def is_trips(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_trips"] = boolen

    @property
    def is_two_pair(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_two_pair"]

    @is_two_pair.setter
    def is_two_pair(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_two_pair"] = boolen

    @property
    def is_pair(self) -> bool:
        return self.hand["hand_rank"]["hand_type"]["is_pair"]

    @is_pair.setter
    def is_pair(self, boolen: bool) -> None:
        self.hand["hand_rank"]["hand_type"]["is_pair"] = boolen

    @property
    def hand_string(self) -> str:
        return self.hand["hand_rank"]["hand_string"]

    @hand_string.setter
    def hand_string(self, string: str) -> None:
        self.hand["hand_rank"]["hand_string"] = string

    @property
    def hand_value(self) -> int:
        return self.hand["hand_rank"]["hand_value"]

    @hand_value.setter
    def hand_value(self, value: int) -> None:
        self.hand["hand_rank"]["hand_value"] = value

    def reset_hand(self) -> None:
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
        hand =[deck.pop() for x in range(5)] if i < number_of_players else []

        if i < number_of_players:

            players[name] = Player(name)
            players[name].cards = hand

            hand_translator(players[name])

            evaluate_hand(players[name])

            if i == number_of_players - 1:
                players[random.choice(list(players.keys()))].dealer = "D"

        else:
            break

    return players

def card_exchange(players: dict, deck: list) -> None:
    for player in players:
        if not players[player].fold:
            hand = players[player].cards.split(' ')
            temp_hand = hand.copy()
            unsuited_hand = players[player].unsuited_cards
            discard_list = []

            if 14 in unsuited_hand:
                max_discard = 4
            else:
                max_discard = 3

            if players[player].name == "Player 1":
                print(("{:<3} {:<3} {:<3} {:<3} {:<3}".format(1, 2, 3, 4, 5)))
                print ("{:<4} {:<4} {:<4} {:<4} {:<4}".format(*hand))

                num_cards_to_discard = int_ck(input(f"How many cards will you discard?\n(Max of {max_discard}): "))

                while num_cards_to_discard > max_discard:
                    num_cards_to_discard = int_ck(input(f"You can only discard upto {max_discard} \n(Max of {max_discard}): "))

                for i in range(num_cards_to_discard):
                    card_index = int_ck(input("Pick card 1-5: "))

                    if 1 <= card_index >=  5 and card_index not in discard_list:
                        discard_list.append(card_index)
                    else:
                        while card_index < 1 or card_index > 5 or card_index in discard_list:
                            card_index = int_ck(input("Card selection must be 1-5\nand must not be a previously discarded card\nNew card selection: "))
                        discard_list.append(card_index)

                for i in discard_list:
                    hand.pop(hand.index(temp_hand[i - 1]))

            else:
                hand_value = players[player].hand_value
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

            players[player].cards = hand

            hand_translator(players[player])

            evaluate_hand(players[player])

def hand_translator(player: Player) -> None:
    player_cards = player.cards.split(" ")
    player_hand_unsuited = player.unsuited_cards
    player_hand_suited = player.suited_cards

    player_hand_unsuited.clear()
    player_hand_suited.clear()

    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11}

    for card in player_cards:
        value = card[:-2]
        player_hand_suited.append(card[-2:])

        if value in card_values:
            player_hand_unsuited.append(card_values[value])
        else:
            player_hand_unsuited.append(int(value))

    if player.name == "Player 1":
        player.npc_cards = player_cards
    else:
        player.npc_cards = "█ █ █ █ █"

def new_hand(players: dict, deck: list) -> None:
    dealer_position = 0

    for player in players.values():
        if player.dealer == "D":
            dealer_position = int(player.name.split()[1])
            player.dealer = ""
            break

    for player in players:
        players[player].reset_hand()

        if players[player].money > 0:
            hand =[deck.pop() for x in range(5)]

            players[player].cards = hand

            hand_translator(players[player])

            evaluate_hand(players[player])
        else:
            if player.name == "Player 1":
                print("GAME OVER")
                exit()
            else:
                players.pop(player.name)

    next_dealer = "Player 1" if dealer_position == len(players) else f"Player {dealer_position +1}"
    players[next_dealer].dealer = "D"

    if len(players) == 1:
        print("YOU WIN")
