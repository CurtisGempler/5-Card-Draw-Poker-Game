import os, time

def print_table(players: dict, pot: dict) -> None:
    os.system('cls')
    print_string = []
    for player in players:
        print_string.clear()
        seat = players[player]
        if seat.name[len(seat.name)-1:] == "1" or seat.name[len(seat.name)-1:] == "6":
            print_string.append(f"{seat.dealer}".center(100))
            print_string.append(f"{seat.name}".center(100))
            print_string.append(f"${seat.money_get()}".center(100))
            print_string.append(f"Bet: {seat.bet_get()}".center(100))
            if seat.name[len(seat.name)-1:] == "1":
                print_string.append(f"{seat.cards_get()}".center(105))
                print_string.append(f"{seat.hand_string_get()}".center(100))
            else:
                print_string.append(f"{seat.npc_cards_get()}".center(100))


            for i in print_string:
                print(i)

        elif int(seat.name[len(seat.name)-1:]) % 2 == 0:
            next_seat = players[f"Player {int(seat.name[len(seat.name)-1:]) + 1}"]
            print_string.append(f"{seat.dealer.ljust(0)}{next_seat.dealer.rjust(100)}")
            print_string.append(f"{seat.name.ljust(0)}{next_seat.name.rjust(100-len(seat.name))}")
            print_string.append(f"${str(seat.money_get()).ljust(0)}{('$' + str(next_seat.money_get())).rjust(100-(len(str(seat.money_get())) + 1))}")
            print_string.append(f"{('Bet: ' + str(seat.bet_get())).ljust(0)}{('Bet: ' + str(next_seat.bet_get())).rjust(100 - len(('Bet: ' + str(seat.bet_get()))))}")
            print_string.append(f"{seat.npc_cards_get().ljust(0)}{next_seat.npc_cards_get().rjust(100-len(seat.npc_cards_get()))}")

            
            for i in print_string:
                print(i)

        if seat.name[len(seat.name)-1:] == "2":
            print_string.clear()
            print_string.append(f"Pot: ${pot['main_pot']}".center(100))
            print_string.append(f"Current Bet: ${pot['current_bet']}".center(100))

            
            for i in print_string:
                print(i)
    time.sleep(.5)

def end_print_table(players: dict, pot: dict) -> None:
    os.system('cls')
    print_string = []
    for player in players:
        print_string.clear()
        seat = players[player]
        if seat.name[len(seat.name)-1:] == "1" or seat.name[len(seat.name)-1:] == "6":
            print_string.append(f"{seat.dealer}".center(100))
            print_string.append(f"{seat.name}".center(100))
            print_string.append(f"${seat.money_get()}".center(100))
            print_string.append(f"Bet: {seat.bet_get()}".center(100))
            if seat.fold_get():
                print_string.append(f"{seat.cards_get()}".center(100))
            else:
                print_string.append(f"{seat.cards_get()}".center(105))
            print_string.append(f"{seat.hand_string_get()}".center(100))

            for i in print_string:
                print(i)

        elif int(seat.name[len(seat.name)-1:]) % 2 == 0:
            next_seat = players[f"Player {int(seat.name[len(seat.name)-1:]) + 1}"]
            print_string.append(f"{seat.dealer.ljust(0)}{next_seat.dealer.rjust(100)}")
            print_string.append(f"{seat.name.ljust(0)}{next_seat.name.rjust(100-len(seat.name))}")
            print_string.append(f"${str(seat.money_get()).ljust(0)}{('$' + str(next_seat.money_get())).rjust(100-(len(str(seat.money_get())) + 1))}")
            print_string.append(f"{('Bet: ' + str(seat.bet_get())).ljust(0)}{('Bet: ' + str(next_seat.bet_get())).rjust(100 - len(('Bet: ' + str(seat.bet_get()))))}")
            if seat.fold_get() and next_seat.fold_get():
                print_string.append(f"{seat.cards_get().ljust(0)}{next_seat.cards_get().rjust(100-len(seat.cards_get()))}")
            elif seat.fold_get() and not next_seat.fold_get():
                print_string.append(f"{seat.cards_get().ljust(0)}{next_seat.cards_get().rjust(105-len(seat.cards_get()))}")
            else:
                print_string.append(f"{seat.cards_get().ljust(0)}{next_seat.cards_get().rjust(110-len(seat.cards_get()))}")
            print_string.append(f"{seat.hand_string_get().ljust(0)}{next_seat.hand_string_get().rjust(100-len(seat.hand_string_get()))}")
            
            for i in print_string:
                print(i)

        if seat.name[len(seat.name)-1:] == "2":
            print_string.clear()
            print_string.append(f"Pot: ${pot['main_pot']}".center(100))
            print_string.append(f"Current Bet: ${pot['current_bet']}".center(100))

            
            for i in print_string:
                print(i)

    time.sleep(.5)

def print_winners(players: dict, pot: dict, winners:list) -> None:
    end_print_table(players, pot)
    
    if len(winners) > 1:
        winnings = pot["main_pot"] / len(winners)
        pot["main_pot"] = 0
        for i in winners:
            players[i].money_set(players[i].money_get() + winnings)        
    else:
        winnings = pot["main_pot"]
        pot["main_pot"] = 0
        players[winners[0]].money_set(players[winners[0]].money_get() + winnings)
    
    end_print_table(players, pot)
    
    if len(winners) > 1:
        print("\n")
        for i in winners:
            print(f"{i} wins with a {players[i].hand_string_get()}")
    else:
        print(f"\n{winners[0]} wins with a {players[winners[0]].hand_string_get()}")

    