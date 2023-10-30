from poker_pkg.validation import bet_choice_ck, bet_amount_ck
from poker_pkg.screens import print_table

def ante(players, pot: dict) -> None:
    for player in players:
        players[player].money_set(players[player].money_get() - 20)
        pot["main_pot"] += 20

def betting_round(players, pot: dict)  -> bool:
    dealer_position = 0

    for player in players:
        if players[player].dealer == "D":
            dealer_position = int(players[player].name[len(players[player].name) - 1:])
            break
    
    player_count = len(players)

    if dealer_position < player_count:
        bet_current_position = dealer_position
    else:
        bet_current_position = 1

    current_bet = pot["current_bet"]
    betting_order = list(players)
    betting_done = False  
    count = 0
    high_bet_player = ""

    while not betting_done:
        
        player = players[betting_order[bet_current_position]]
        player_curent_bet = player.bet_get()

        if player.name != high_bet_player:
            if not player.fold:
                if current_bet == 0 or player_curent_bet != current_bet:
                    if player.name == "Player 1":
                        player_choice = 0
                        if current_bet == 0:
                            player_choice = bet_choice_ck(input("\n1. Bet\n2. Fold\nChoose: "), 2)
                            if player_choice == 1:
                                current_bet = bet(player, bet_amount_ck(player, input("How much would you like to bet?\n(Max: 100):")), pot)
                                high_bet_player = player.name
                            elif player_choice == 2:
                                fold(player)
                        else:
                            player_choice = bet_choice_ck(input(f"\n1. Call ${current_bet - player.bet_get()}\n2. Fold\n3. Raise\nChoose: "), 3)
                            if player_choice == 1:
                                call_bet(player, current_bet, pot)
                            elif player_choice == 2:
                                fold(player)
                            else:
                                current_bet = raise_bet(player, current_bet, bet_amount_ck(player, input("How much would you like to raise by?\n(Max: 100):")), pot)
                                high_bet_player = player.name
                    else:
                        player_hand_value = player.hand_value_get()
                        if current_bet == 0:
                            if player_hand_value >= 1 and player_hand_value <= 3:
                                current_bet = bet(player, 20, pot)
                                high_bet_player = player.name
                            elif player_hand_value >= 3 and player_hand_value  <= 6:
                                current_bet = bet(player, 40, pot)
                                high_bet_player = player.name
                            elif player_hand_value >= 6 and player_hand_value  <= 8:
                                current_bet = bet(player, 60, pot)
                                high_bet_player = player.name
                            else:
                                current_bet = bet(player, 100, pot)
                                high_bet_player = player.name
                        else:
                            if player_hand_value  >= 1 and player_hand_value <= 3:
                                if current_bet > 40:
                                    fold(player)
                                else: 
                                    call_bet(player, current_bet, pot)
                            elif player_hand_value >= 3 and player_hand_value  <= 6:
                                if current_bet < 60:
                                    current_bet = raise_bet(player, current_bet, 60 - current_bet, pot)
                                    high_bet_player = player.name
                                elif current_bet <= 80:
                                    call_bet(player, current_bet, pot)
                                else:
                                    fold(player)
                            elif player_hand_value >= 6 and player_hand_value  <= 8:
                                if current_bet < 80:
                                    current_bet = raise_bet(player, current_bet, 80 - current_bet, pot)
                                    high_bet_player = player.name
                                elif current_bet <= 100:
                                    call_bet(player, current_bet, pot)
                                else:
                                    fold(player)
                            else:
                                if current_bet < 100:
                                    current_bet = raise_bet(player, current_bet, 100 - current_bet, pot)
                                    high_bet_player = player.name
                                else:
                                    call_bet(player, current_bet, pot)

        if bet_current_position < player_count - 1:
            bet_current_position += 1
        else:
            bet_current_position = 0

        count += 1
        betting_done = False
        if player.name == high_bet_player: 
            for seat in players:
                if players[seat].bet_get() == current_bet or players[seat].fold_get():
                    betting_done = True
                else:
                    betting_done = False
                    break
            count = 0

        if betting_done:
            fold_count = 0
            for seat in players:
                if players[seat].fold == True:
                    fold_count += 1
            if fold_count == player_count - 1:
                return True
            for seat in players:
                players[seat].bet_set(0)

        print_table(players, pot)

def call_bet(player, current_bet: int, pot: dict) -> None:
    player_money = player.money_get()
    player_curent_bet = player.bet_get()
    if current_bet - player_curent_bet < player_money:
        pot["main_pot"] += current_bet - player_curent_bet
        player.money_set(player_money - (current_bet - player_curent_bet))
        player.bet_set(current_bet)
    else:
        print("You don't have enough money to call.")
        fold(player)

def fold(player) -> None:
    player.fold_set()

def bet(player, bet: int, pot: dict) -> int:
    player.bet_set(bet)
    player.money_set(player.money_get() - bet)
    pot["main_pot"] += bet
    return bet

def raise_bet(player, current_bet: int, bet: int, pot: dict) -> int:
    current_bet += bet
    pot["main_pot"] += current_bet
    player.money_set(player.money_get() - current_bet)
    player.bet_set(current_bet)
    return current_bet