
def evaluate_hand(player) -> None:
    unsuited_hand = player.unsuited_cards_get()
    suited_hand = player.suited_cards_get()
    high_card = max(unsuited_hand)
    card_value_translator = {14: "Ace",13: "King",12: "Queen",11: "Jack",10: "10",9: "9",8: "8",7: "7",6: "6",5: "5",
                             4: "4",3: "3",2: "2",}

    unsuited_occurance_len = len(list(set([x for i,x in enumerate(unsuited_hand) if unsuited_hand.count(x) > 1])))
    unsuited_occurance = {item: unsuited_hand.count(item) for item in unsuited_hand}
    
    # Flush check
    if len(list(set([x for i,x in enumerate(suited_hand) if suited_hand.count(x) == 5]))):
        player.is_flush_set(True)

    # Straight check
    if 14 in unsuited_hand:
        temp = unsuited_hand.copy()
        
        for i in range(len(temp)):
            if temp[i] == 14:
                temp[i] = 1
        temp.sort()

        if sorted(unsuited_hand) == list(range(min(unsuited_hand),max(unsuited_hand)+1)) or sorted(temp) == list(range(min(temp),max(temp)+1)):
            player.is_straight_set(True) 

    elif sorted(unsuited_hand) == list(range(min(unsuited_hand),max(unsuited_hand)+1)):
        player.is_straight_set(True) 
    
    # Check for Pair, Two Pair, Three of a kind, Full House, or Quads
    if unsuited_occurance_len > 0:
        if 4 in unsuited_occurance.values():
            player.is_quads_set(True)
        elif 3 in unsuited_occurance.values() and 2 in unsuited_occurance.values():
            player.is_full_house_set(True)
        elif 3 in unsuited_occurance.values():
            player.is_trips_set(True)
        elif 2 in unsuited_occurance.values():
            if unsuited_occurance_len > 1:
                player.is_two_pair_set(True)
            else:
                player.is_pair_set(True)

    # Best hand determination
    if player.is_flush_get() and player.is_straight_get() and high_card == 14:
        player.hand_string_set(f"Royal Flush {suited_hand[0]}'s")
        player.hand_value_set(10)
    elif player.is_flush_get() and player.is_straight_get():
        player.hand_string_set("Straight Flush")
        player.hand_string_set(f"Straight Flush {card_value_translator[high_card]} high.")
        player.hand_value_set(9)
    elif player.is_quads_get():
        hand_string = ''
        for card in unsuited_occurance:
            if unsuited_occurance[card] > 1:
                hand_string += f" {card_value_translator[card]}'s"
        player.hand_string_set(f"Four of a Kind{hand_string}")
        player.hand_value_set(8)
    elif player.is_full_house_get():
        hand_string = ''
        for card in sorted(list(unsuited_occurance), reverse = True):
            if unsuited_occurance[card] > 1:
                hand_string += f" {card_value_translator[card]}'s"
        player.hand_string_set("Full House")
        player.hand_value_set(7)
    elif player.is_flush_get():
        player.hand_string_set(f"Flush {card_value_translator[high_card]} high.")
        player.hand_value_set(6)
    elif player.is_straight_get():
        player.hand_string_set(f"Straight {card_value_translator[high_card]} high.")
        player.hand_value_set(5)
    elif player.is_trips_get():
        hand_string = ''
        for card in unsuited_occurance:
            if unsuited_occurance[card] > 1:
                hand_string += f" {card_value_translator[card]}'s"
        player.hand_string_set(f"Three of a Kind{hand_string}")
        player.hand_value_set(4)
    elif player.is_two_pair_get():
        hand_string = ''
        for card in sorted(list(unsuited_occurance), reverse = True):
            if unsuited_occurance[card] > 1:
                hand_string += f" {card_value_translator[card]}'s"
        player.hand_string_set(f"Two Pair{hand_string}")
        player.hand_value_set(3)
    elif player.is_pair_get():
        hand_string = ''
        for card in unsuited_occurance:
            if unsuited_occurance[card] > 1:
                hand_string += f" {card_value_translator[card]}'s"
        player.hand_string_set(f"Pair{hand_string}")
        player.hand_value_set(2)
    else:
        player.hand_string_set(f"High Card {card_value_translator[high_card]}")
        player.hand_value_set(1)

def hand_comparision(players: dict) -> list:
    high_hand_player = [players["Player 1"].name]
    for player in players:
        high_hand_value = players[high_hand_player[0]].hand_value_get()
        high_hand_unsuited = players[high_hand_player[0]].unsuited_cards_get()
        high_hand_unsuited.sort(reverse = True)
        high_hand_suits = players[high_hand_player[0]].suited_cards_get()
        
        player_hand_value = players[player].hand_value_get()
        player_name = players[player].name
        player_hand_unsuited = players[player].unsuited_cards_get()
        player_hand_unsuited.sort(reverse = True)
        player_hand_suits = players[player].suited_cards_get()

        if players[player].name == "Empty Seat":
            break
        elif players[player].name == "Player 1":
            continue
        else:
            if high_hand_value < player_hand_value:
                set_high_hand_player(1, player_name, high_hand_player)

            elif high_hand_value == player_hand_value:
                if  high_hand_value == 1:
                    set_high_hand_player(high_card(high_hand_unsuited,player_hand_unsuited),player_name, high_hand_player)

                elif high_hand_value == 2:
                    set_high_hand_player(pair(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 3:
                    set_high_hand_player(tow_pair(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 4:
                    set_high_hand_player(three_of_a_kind(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 5:
                    set_high_hand_player(straight(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 6:
                    set_high_hand_player(flush(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 7:
                    set_high_hand_player(full_house(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 8:
                    set_high_hand_player(four_of_a_kind(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 9:
                    set_high_hand_player(straight_flush(high_hand_unsuited, player_hand_unsuited),player_name,high_hand_player)

                elif high_hand_value == 10:
                    set_high_hand_player(royal_flush(high_hand_suits[0], player_hand_suits[0]),player_name,high_hand_player)
                    
    return (high_hand_player)

def set_high_hand_player(x: int, name: str, high_hand_player: str) -> None:
    if x == 1:
        high_hand_player.clear()
        high_hand_player.append(name)
    elif x == 2:
        high_hand_player.append(name)   

def high_card(high_hand: list, player_hand: list) -> int:
                    
    for card in range(len(high_hand)-1):
        identical_hands = False
        if high_hand[card] > player_hand[card]:
            return 0
        elif high_hand[card] < player_hand[card]:
            return 1
        else:
            identical_hands = True
            continue
    
    if identical_hands: 
        return 2
    
def pair(high_hand: list, player_hand: list) -> int:
    high_player_unsuited_occurance = list(set([x for i,x in enumerate(high_hand) if high_hand.count(x) > 1]))
    player_unsuited_occurance = list(set([x for i,x in enumerate(player_hand) if player_hand.count(x) > 1]))

    if high_player_unsuited_occurance[0] > player_unsuited_occurance[0]:
        return 0
    elif high_player_unsuited_occurance[0] < player_unsuited_occurance[0]:
        return 1
    else:
        high_hand_temp = list(filter(lambda i: i not in high_player_unsuited_occurance, high_hand))
        player_temp_hand = list(filter(lambda i: i not in player_unsuited_occurance, player_hand))
        return high_card(high_hand_temp, player_temp_hand)
    
def tow_pair(high_hand: list, player_hand: list) -> int:
    high_player_unsuited_occurance = sorted(list(set([x for i,x in enumerate(high_hand) if high_hand.count(x) > 1])), reverse = True)
    player_unsuited_occurance = sorted(list(set([x for i,x in enumerate(player_hand) if player_hand.count(x) > 1])), reverse = True)

    for card in range(len(high_player_unsuited_occurance)-1):
        identical_hands = False
        if high_player_unsuited_occurance[card] > player_unsuited_occurance[card]:
            return 0
        elif high_player_unsuited_occurance[card] < player_unsuited_occurance[card]:
            return 1
        else:
            identical_hands = True
            continue
    
    if identical_hands == True:
        high_hand_temp = list(filter(lambda i: i not in high_player_unsuited_occurance, high_hand))
        player_temp_hand = list(filter(lambda i: i not in player_unsuited_occurance, player_hand))
        return high_card(high_hand_temp, player_temp_hand)
    
def three_of_a_kind(high_hand: list, player_hand: list) -> int:
    return pair(high_hand, player_hand)

def straight(high_hand: list, player_hand: list) -> int:
    return high_card(high_hand, player_hand)

def flush(high_hand: list, player_hand: list) -> int:
    return high_card(high_hand, player_hand)

def full_house (high_hand: list, player_hand: list) -> int:
    high_player_unsuited_occurance = list(set([x for i,x in enumerate(high_hand) if high_hand.count(x) == 3]))
    player_unsuited_occurance = list(set([x for i,x in enumerate(player_hand) if player_hand.count(x) == 3]))

    if high_player_unsuited_occurance[0] > player_unsuited_occurance[0]:
        return 0
    elif high_player_unsuited_occurance[0] < player_unsuited_occurance[0]:
        return 1
    
def four_of_a_kind(high_hand: list, player_hand: list) -> int:
    return pair(high_hand, player_hand)

def straight_flush(high_hand: list, player_hand: list) -> int:
    return high_card(high_hand, player_hand)

def royal_flush(high_hand: str, player_hand: str) -> int:
    suits = {"♠️": 1,"♥️": 2,"♦️": 3,"♣️": 4}
    high_hand_value = suits[high_hand]
    player_hand_value = suits[player_hand]

    if high_hand_value > player_hand_value:
        return 0
    else:
        return 1