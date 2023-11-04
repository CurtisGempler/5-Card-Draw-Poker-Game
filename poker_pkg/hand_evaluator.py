"""Module providing poker hand evaluation and value assignment"""
from collections import Counter

def evaluate_hand(player) -> None:
    # Local varible population
    unsuited_hand = player.unsuited_cards_get()
    suited_hand = player.suited_cards_get()
    hand_high_card = max(unsuited_hand)
    unsuited_occurance = {item: unsuited_hand.count(item) for item in unsuited_hand} # Returns dict with keys of list values and number of occurances
    card_value_translator = {14: "Ace",13: "King",12: "Queen",11: "Jack",10: "10",9: "9",8: "8",7: "7",6: "6",5: "5",
                             4: "4",3: "3",2: "2",}

    # Player set attribute function 
    def set_hand(hand_string, hand_value):
        player.hand_string_set(hand_string)
        player.hand_value_set(hand_value)

    # Flush check
    def is_flush() -> bool:
        return len(set(suited_hand)) == 1

    # Straight check
    def is_straight() -> bool:
        if 14 in unsuited_hand:
            temp_hand = sorted([1 if card == 14 else card for card in unsuited_hand])
            return sorted(unsuited_hand) == list(range(min(unsuited_hand),max(unsuited_hand)+1)) or sorted(temp_hand) == list(range(min(temp_hand),max(temp_hand)+1))
        return sorted(unsuited_hand) == list(range(min(unsuited_hand),max(unsuited_hand)+1))

    # Quads check
    def is_quads() -> bool:
        return 4 in unsuited_occurance.values()

    # Full House check
    def is_full_house() -> bool:
        return 3 in unsuited_occurance.values() and 2 in unsuited_occurance.values()

    # Three of a Kind check
    def is_trips() -> bool:
        return 3 in unsuited_occurance.values()

    # Two Pair check
    def is_two_pair() -> bool:
        return list(unsuited_occurance.values()).count(2) > 1

    # Pair check
    def is_pair() -> bool:
        return list(unsuited_occurance.values()).count(2) == 1

    # Best hand determination
    if is_flush() and is_straight():
        if hand_high_card == 14:
            set_hand(f"Royal Flush {card_value_translator[hand_high_card]}'s", 10)
        else:
            set_hand(f"Straight Flush {card_value_translator[hand_high_card]} high.", 9)
    elif is_quads():
        set_hand(f"Four of a Kind {card_value_translator[max(unsuited_occurance, key = unsuited_occurance.get)]}'s", 8)
    elif is_full_house():
        set_hand(f"Full House {card_value_translator[max(unsuited_occurance, key = unsuited_occurance.get)]}'s over {card_value_translator[min(unsuited_occurance, key = unsuited_occurance.get)]}'s", 7)
    elif is_flush():
        set_hand(f"Flush {card_value_translator[hand_high_card]}'s", 6)
    elif is_straight():
        set_hand(f"Straight {card_value_translator[hand_high_card]} high", 5)
    elif is_trips():
        set_hand(f"Three of a Kind {card_value_translator[max(unsuited_occurance, key = unsuited_occurance.get)]}'s", 4)
    elif is_two_pair():
        max_card = max(unsuited_occurance, key=unsuited_occurance.get)
        set_hand(f"Two Pair {card_value_translator[max_card]}'s and {card_value_translator[min(unsuited_occurance, key = unsuited_occurance.get)]}'s", 3)
    elif is_pair():
        max_card = max(unsuited_occurance, key=unsuited_occurance.get)
        set_hand(f"Pair {card_value_translator[max_card]}'s", 2)
    else:
        set_hand(f"High Card {card_value_translator[hand_high_card]}", 1)

def hand_comparision(players: dict) -> list:
    # Sets High Player
    def set_high_hand_player(x: int, player_name: str) -> None:
        if x == 1:
            high_hand_player.clear()
            high_hand_player.append(player_name)
        elif x == 2:
            high_hand_player.append(player_name)

    # Returns sorted list of unsuited cards
    def get_sorted_unsuited_hand(player) -> list:
        return sorted(player.unsuited_cards_get(), reverse = True)

    # Compares player hand lists in order of highest to lowest
    def compare_hands(high_hand: list, player_hand: list) -> int:
        for high_hand_card, player_hand_card in zip(high_hand, player_hand):
            if high_hand_card > player_hand_card:
                return 0
            if high_hand_card < player_hand_card:
                return 1
        return 2

    # Counts recurring cards then returns filtered list of cards with multipuls
    def card_occurance(hand: list)-> list:
        card_counts = Counter(hand)
        max_count = max(card_counts.values())
        max_cards = [card for card, count in card_counts.items() if count == max_count]
        return sorted(max_cards, reverse = True)

    # Initial High Player settings
    high_hand_player = ["Player 1"]
    high_hand = get_sorted_unsuited_hand(players["Player 1"])
    high_hand_value = players["Player 1"].hand_value_get()

    for player_name, player in players.items():

        if player_name == "Player 1" or player.hand_value_get() == 0:
            continue

        # Local Player settings
        player_hand_value = player.hand_value_get()
        player_hand = get_sorted_unsuited_hand(player)

        # Hand Value comparison 
        if high_hand_value < player_hand_value:
            set_high_hand_player(1, player_name)
        elif high_hand_value == player_hand_value:
            # High Card comparison in event of matching hand values
            if  high_hand_value in (1, 5, 9):
                set_high_hand_player(compare_hands(high_hand, player_hand),player_name)
            # High pair, two pair, trips, quads, and full house comparison in event of matching hand values
            elif high_hand_value in (2, 3, 4, 7, 8):
                set_high_hand_player(compare_hands(card_occurance(high_hand), card_occurance(player_hand)),player_name)
            # Royal Flush suit comparison in event of matching hand values
            elif high_hand_value == 10:
                high_hand_suits = players[high_hand_player[0]].suited_cards_get()
                player_hand_suits = player.suited_cards_get()
                suits = {"♠️": 1,"♥️": 2,"♦️": 3,"♣️": 4}
                if suits[high_hand_suits[0]] < suits[player_hand_suits[0]]:
                    set_high_hand_player(1, player_name)

        high_hand_value = players[high_hand_player[0]].hand_value_get()

    return (high_hand_player)