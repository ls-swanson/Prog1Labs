import p1_random as p1
rng = p1.P1Random()

user_input = 0
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

while (user_input != 4):
    user_total = 0
    game_num += 1
    print(f'START GAME #{game_num}')
    first_card = rng.next_int(13) + 1
    if first_card == 1:
        print("\nYour card is a ACE!")
        user_total += 1
    elif 2 <= first_card <= 10:
        print(f'\nYour card is a {first_card}!')
        user_total += first_card
    elif first_card == 11:
        print("\nYour card is a JACK!")
        user_total += 10
    elif first_card == 12:
        print("\nYour card is a QUEEN!")
        user_total += 10
    elif first_card == 13:
        print("\nYour card is a KING!")
        user_total += 10
    print(f'Your hand is: {user_total}\n')

    print("1. Get another card\n"
          "2. Hold hand\n"
          "3. Print statistics\n"
          "4. Exit\n")

    user_input = int(input("Choose an option: "))

    while not(user_input == 2 or user_input == 4):
        if (user_input == 1):
            second_card = rng.next_int(13) + 1
            if second_card == 1:
                print("\nYour card is a ACE!")
                user_total += 1
            elif 2 <= second_card <= 10:
                print(f'\nYour card is a {second_card}!')
                user_total += second_card
            elif second_card == 11:
                print("\nYour card is a JACK!")
                user_total += 10
            elif second_card == 12:
                print("\nYour card is a QUEEN!")
                user_total += 10
            elif second_card == 13:
                print("\nYour card is a KING!")
                user_total += 10
            print(f'Your hand is: {user_total}\n')

            if (user_total == 21):
                print("BLACKJACK! You win!\n")
                player_wins += 1
                break
            elif (user_total > 21):
                print("You exceeded 21! You lose.\n")
                dealer_wins += 1
                break
        elif (user_input == 3):
            print(f'\nNumber of Player wins: {player_wins}')
            print(f'Numer of Dealer wins: {dealer_wins}')
            print(f'Number of tie games: {tie_games}')
            total_games = player_wins + dealer_wins + tie_games
            win_percent = player_wins / total_games * 100
            print(f'Total # of games played is: {total_games}')
            print(f'Percentage of Player wins: {win_percent:.1f}%\n')
        else:
            print("Invalid input!\n")
            print("Please enter an integer value between 1 and 4.")

        print("1. Get another card\n"
              "2. Hold hand\n"
              "3. Print statistics\n"
              "4. Exit\n")

        user_input = int(input("Choose an option: "))

    if (user_input == 2):
        dealer_total = rng.next_int(11) + 16
        print(f"\nDealer's hand: {dealer_total}")
        print(f'Your hand is: {user_total}\n')
        if (dealer_total > 21 or dealer_total < user_total):
            print("You win!\n")
            player_wins += 1
        elif (dealer_total == user_total):
            print("It's a tie! No one wins!\n")
            tie_games += 1
        elif (dealer_total > user_total):
            print("Dealer wins!\n")
            dealer_wins += 1
    elif (user_input == 4):
        break
