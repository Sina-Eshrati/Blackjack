from art import logo
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards_list):
    if len(cards_list) == 2 and sum(cards_list) == 21:
        return "Blackjack"
    elif 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
        return sum(cards_list)
    else:
        return sum(cards_list)

def play_game():
    print(logo)
    player_cards = []
    dealer_cards = []
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    game_continued = True
    draw_another_card = 'y'
    while game_continued:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"   Your cards: {player_cards}, current Score: {player_score}")
        print(f"   Dealer's first card: {dealer_cards[0]}")
        if player_score == dealer_score == "Blackjack":
            print("Draw")
            game_continued = False
        elif player_score == "Blackjack":
            print("You won with a blackjack")
            game_continued = False
        elif dealer_score == "Blackjack":
            print("Dealer won with a blackjack")
            game_continued = False
        elif player_score > 21:
            print("You lost! The score is over 21")
            game_continued = False
        elif dealer_score > 21:
            print("Dealer lost! The score is over 21")
            game_continued = False
        elif draw_another_card == 'y':
            draw_another_card = input("Type 'y' to get another card or type 'n' to pass: ")
            if draw_another_card == 'y':
                player_cards.append(deal_card())
            else:
                while dealer_score < 17:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)
                print(f"   Your final hand: {player_cards}, Final score: {player_score}")
                print(f"   Dealer's final hand: {dealer_cards}, Final score: {dealer_score}")
                if dealer_score > 21:
                    print("Dealer lost! The score is over 21")
                elif player_score > dealer_score:
                    print("You won")
                elif dealer_score > player_score:
                    print("Dealer won")
                else:
                    print("Draw")
                game_continued = False

while input("Do you want to play a game of Blackjack? (Type 'y' or 'n') ") == 'y':
    clear()
    play_game()




