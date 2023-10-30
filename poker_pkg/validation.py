def int_ck(user_input) -> int:
    try:
        user_input = int(user_input)
        return user_input
    
    except:
        return int_ck(input("Input must be a number: "))
            
def player_ck(user_input) -> int:
        user_input = int_ck(user_input)
     
        if user_input >= 2 and user_input <= 6:
            return user_input
        else:
            return player_ck(input("Number must be between 2-6\n(Max 6) How Many Players 2-6: "))
        
def bet_choice_ck(user_input, num_choises: int) -> int:
     user_input = int_ck(user_input)

     if user_input >= 1 and user_input <= 3:
          return user_input
     else:
          return bet_choice_ck(input(f"Number must be 1-{num_choises}"), num_choises)
     
def bet_amount_ck(player, bet) -> int:
     player_money = player.money_get()
     bet = int_ck(bet)
     if player_money >= bet and bet <= 100:
          return bet
     elif bet > 100:
          return bet_amount_ck(player, input(f"Bet must be less than $100 \nBet (Max) $100"))
     else:
          return bet_amount_ck(player, input(f"Bet must be less than your available money ${player_money}\nBet (Max) $100"))
     
def y_n_ck(user_input):
     if user_input.lower() == 'y' or user_input.lower() == 'n':
          return user_input.lower()
     else:
          return y_n_ck(input("Please choose Y or N"))