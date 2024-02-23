print("""The Game of Blackjack: 
> This is a wonderful card game. The goal is to have cards whose value is more than the dealer's cards but not more the '21'.
> If you go over 21, you have "Busted" and lost the game against the dealer. And the same can happen to the dealer.
> The numbers have their face value. Jack, Queen and King have a value of 10 each. And Ace has a value from 1 to 11, based on the player's choice.
> The dealer deals the first cards to him and the player. The dealer's first card is unknown. 
> Again, a second card is given to both. This time the player can see the dealer's card.
> The player has to decide to stay or hit. 
    'Staying' means that you don't want to dealer to give you another card.
    'Hitting' means that you want the dealer to give you another card. You can hit as many times as you want, until you "stay" or "bust".
> At the last, the dealer flips over his first card. If his total is 16 or lower, then the dealer deals himself another card.
""")

import random

# Create a deck of cards.
suits = ["Hearts","Clubs","Spades","Diamonds"]
deck_list = []

for suit in suits:
    for card_number in range(13):
        if card_number == 0: 
            deck_list.append(f"Ace of {suit}")
        elif card_number == 10: 
            deck_list.append(f"Jack of {suit}")
        elif card_number == 11: 
            deck_list.append(f"Queen of {suit}")
        elif card_number == 12: 
            deck_list.append(f"King of {suit}")
        else:
            deck_list.append(f"{card_number+1} of {suit}")

# Let's shuffle the deck.
random.shuffle(deck_list)

print("Let's start the game.")
dealer = ["d"]
player = ["p"]
dealer_value = 0
player_value = 0
has_won = False
has_lost = False
dealer_busted = False
player_busted = False
stay_chosen = False
dealer_card_count = 0

# Dealing a card
def deal_card(player_name: list[str]):
    global dealer_card_count

    str_player_name = ""

    if (player_name[0])== 'p':
        str_player_name = "player"
    elif (player_name[0]) == "d":
        dealer_card_count += 1
        str_player_name = "Dealer"

    dealt_card = random.randrange(0,len(deck_list))

    player_name.append(deck_list[dealt_card])

    if str_player_name == "player":
        print(f"\nThe {str_player_name} has been dealt {deck_list[dealt_card]}")
        player_hand = player.copy()
        player_hand.pop(0)
        print(f"Your hand: {player_hand}")
    elif str_player_name == "Dealer" and dealer_card_count > 1:
        print(f"The {str_player_name} has been dealt {deck_list[dealt_card]}")

    deck_list.pop(dealt_card)


# The first dealing.
print("\nThe first dealing...")
deal_card(dealer)
print("The dealer has been dealt some unknown card.")
deal_card(player)

# Second Dealing.
print("\nThe second dealing...")
deal_card(dealer)
deal_card(player)

# Calculating the value of the cards in hand :
def calculate_cards_value(player_deck):
    duplicate_player_deck = player_deck.copy()
    duplicate_player_deck.pop(0)
    hand_value = 0
    #Resetting player's value

    for card in duplicate_player_deck:
        if "Jack" in card:
            hand_value += 10
        elif "Queen" in card:
            hand_value += 10
        elif "King" in card:
            hand_value += 10
        elif "Ace" in card: 
            pass
        else:
            position_of_space = card.find(" ")
            hand_value += int(card[0:position_of_space])
    
    for card in duplicate_player_deck:

        if player_deck[0] == "d":
            if "Ace" in card:
                if hand_value < 21 :
                    if (21-player_value) <= 11:
                        hand_value = 21
                    else:
                        hand_value += 11
        else:
            if "Ace" in card:
                player_choice = int(input("What is your Ace's value? "))
                if player_choice > 0 and player_choice < 12: 
                    hand_value += player_choice

    return hand_value

# To show dealer's hand at the last.
def show_dealer_hand():
    dealer_hand = dealer.copy()
    dealer_hand.pop(0)
    print(f"Dealer's hand: {dealer_hand}")

# Function of evaluate winner, if the player chooses to stay.
def evaluate_winner():
    global dealer_value
    global player_value
    global dealer_busted
    global player_busted
    global has_won
    global has_lost


    if dealer_value == 0:
        dealer_value = calculate_cards_value(dealer)
    
    if player_value == 0:
        player_value = calculate_cards_value(player)
    

    if player_value == 21:
        if dealer_value == 21:
            show_dealer_hand()
            has_won = True
            print("\nIt's a draw. Both players have a blackjack.")
        else:
            show_dealer_hand()
            has_won = True
            print("\nThe player has a blackjack, and has won the game!")
    else:
        if dealer_value < 16:
            deal_card(dealer)
            dealer_value = calculate_cards_value(dealer)


        if dealer_value > 21:
            dealer_busted = True
            if player_value > 21:
                show_dealer_hand()
                has_lost = True
                print("\nBoth, the player and the dealer busted, but the player lost the game. It's not a draw. >v<")
                player_busted = True
            else:
                show_dealer_hand()
                has_won = True
                print("\nThe dealer has busted and the Player has won the game.")
        elif dealer_value == 21:
            has_lost = True
            show_dealer_hand()
            print("\nThe dealer has a black jack. You have lost the game.")
        elif player_value > dealer_value:
            show_dealer_hand()
            print(f"\nPlayer's value: {player_value}")
            print(f"Dealer's value: {dealer_value}")
            print("\nThe player has won the game.")
            has_won = True
        elif player_value == dealer_value:
            show_dealer_hand()
            print(f"\nPlayer's value: {player_value}")
            print(f"Dealer's value: {dealer_value}")
            print("\nIt's a draw.")
            has_lost = True
        else:
            show_dealer_hand()
            print(f"\nPlayer's value: {player_value}")
            print(f"Dealer's value: {dealer_value}")
            print("\nThe player has lost the game.")
            has_lost = True
            

# Accounting for the Lucky automatic win.
# Using "item" instead of "card", because "card" has already been used above.
is_Ace_there = False
for item in player:
    if "Ace" in item:
        is_Ace_there = True

for item in player:
    if is_Ace_there == True:
        if "Jack" in item or "10" in item or "Queen" in item or "King" in item: 
            player_value == 21
            dealer_value= calculate_cards_value(dealer)
            has_won = True

            if dealer_value == 21:
                show_dealer_hand()
                print("\nIt's a rare draw. Both, the player and dealer have a blackjack already.")
            else:
                show_dealer_hand()
                print("\nPlayer has won with a blackjack in hand.")

while player_value <= 21 and has_won == False and has_lost == False:
    if player_value < 21:
        if stay_chosen == False:
            decision = input('\nWhat is your choice: "hit" or "stay"? ')
            print("\n")

            if decision == "stay":
                stay_chosen = True
            elif decision == "hit":
                deal_card(player)
                player_value = calculate_cards_value(player)
        else: 
            evaluate_winner()
    elif player_value == 21:
        evaluate_winner()
else:
    if player_value > 21:
        player_busted = True
        show_dealer_hand()
        print("\nYou have exceeded 21, and lost the game.")
    elif dealer_busted == True:
        pass
    elif has_won == True:
        pass
    else:
        pass

ending = input("\nPress Enter to exit...")
    