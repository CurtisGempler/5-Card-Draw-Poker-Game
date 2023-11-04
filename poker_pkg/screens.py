import os, time

def print_table(players: dict, pot: dict) -> None:
    os.system('cls')
    print_string = []
    for player in players:
        print_string.clear()
        seat = players[player]

        if seat.name.endswith(("1", "6")):
            print_string.extend([
                f"{seat.dealer}".center(100),
                f"{seat.name}".center(100),
                f"${seat.money}".center(100),
                f"Bet: {seat.bet}".center(100)
            ])
            if seat.name.endswith("1"):
                print_string.extend([
                    f"{seat.cards}".center(105),
                    f"{seat.hand_string}".center(100)
                ])
            else:
                print_string.append(f"{seat.npc_cards}".center(100))


            for i in print_string:
                print(i)

        elif int(seat.name[-1]) % 2 == 0:
            next_seat = players[f"Player {int(seat.name[-1]) + 1}"]
            print_string.extend([
                f"{seat.dealer}{next_seat.dealer.rjust(100)}",
                f"{seat.name}{next_seat.name.rjust(100 - len(seat.name))}",
                f"${str(seat.money)}{('$' + str(next_seat.money)).rjust(100-(len(str(seat.money)) + 1))}",
                f"{('Bet: ' + str(seat.bet))}{('Bet: ' + str(next_seat.bet)).rjust(100 - len(('Bet: ' + str(seat.bet))))}",
                f"{seat.npc_cards}{next_seat.npc_cards.rjust(100-len(seat.npc_cards))}"
            ])

            for i in print_string:
                print(i)

        if seat.name.endswith("2"):
            print_string.clear()
            print_string.extend([
                f"Pot: ${pot['main_pot']}".center(100),
                f"Current Bet: ${pot['current_bet']}".center(100)
            ])

            for i in print_string:
                print(i)

    time.sleep(.5)

def end_print_table(players: dict, pot: dict) -> None:
    os.system('cls')
    print_string = []

    for player in players:
        print_string.clear()
        seat = players[player]

        if seat.name.endswith(("1", "6")):
            print_string.extend([
                f"{seat.dealer}".center(100),
                f"{seat.name}".center(100),
                f"${seat.money}".center(100),
                f"Bet: {seat.bet}".center(100)
            ])

            if seat.fold:
                print_string.append(f"{seat.cards}".center(100))
            else:
                print_string.append(f"{seat.cards}".center(105))

            print_string.append(f"{seat.hand_string}".center(100))

            for i in print_string:
                print(i)

        elif int(seat.name[-1]) % 2 == 0:
            next_seat = players[f"Player {int(seat.name[-1]) + 1}"]

            print_string.extend([
                f"{seat.dealer}{next_seat.dealer.rjust(100)}",
                f"{seat.name}{next_seat.name.rjust(100 - len(seat.name))}",
                f"${str(seat.money)}{('$' + str(next_seat.money)).rjust(100 - (len(str(seat.money)) + 1))}",
                f"{('Bet: ' + str(seat.bet))}{('Bet: ' + str(next_seat.bet)).rjust(100 - len(('Bet: ' + str(seat.bet))))}"
            ])

            if seat.fold and next_seat.fold:
                print_string.append(f"{seat.cards}{next_seat.cards.rjust(100 - len(seat.cards))}")
            elif seat.fold and not next_seat.fold:
                print_string.append(f"{seat.cards}{next_seat.cards.rjust(105 - len(seat.cards))}")
            else:
                print_string.append(f"{seat.cards}{next_seat.cards.rjust(110 - len(seat.cards))}")

            print_string.append(f"{seat.hand_string}{next_seat.hand_string.rjust(100 - len(seat.hand_string))}")

            for i in print_string:
                print(i)

        if seat.name.endswith("2"):
            print_string.clear()
            print_string.extend([
                f"Pot: ${pot['main_pot']}".center(100),
                f"Current Bet: ${pot['current_bet']}".center(100)
            ])

            for i in print_string:
                print(i)

    time.sleep(.5)

def print_winners(players: dict, pot: dict, winners:list) -> None:
    end_print_table(players, pot)

    if len(winners) > 1:
        winnings = pot["main_pot"] / len(winners)
        pot["main_pot"] = 0
        for i in winners:
            players[i].money = players[i].money + winnings
    else:
        winnings = pot["main_pot"]
        pot["main_pot"] = 0
        players[winners[0]].money = players[winners[0]].money + winnings

    end_print_table(players, pot)

    if len(winners) > 1:
        print("\n")
        for i in winners:
            print(f"{i} wins with a {players[i].hand_string}")
    else:
        print(f"\n{winners[0]} wins with a {players[winners[0]].hand_string}")
        