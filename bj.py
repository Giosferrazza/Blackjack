import random

class MoneySystem:
    def __init__(self):
        # Initialize an empty dictionary to store currency amounts
        self.wallet = {}

    def add_money(self, currency, amount):
        # Add or update the amount of a specific currency in the wallet
        if currency in self.wallet:
            self.wallet[currency] += amount
        else:
            self.wallet[currency] = amount

    def remove_money(self, currency, amount):
        # Remove a specific amount of currency from the wallet
        if currency in self.wallet:
            if self.wallet[currency] >= amount:
                self.wallet[currency] -= amount
            else:
                print(f"Not enough {currency} in the wallet.")
        else:
            print(f"{currency} not found in the wallet.")

    def check_balance(self):
        # Display the current balance of the wallet
        print("Wallet Balance:")
        for currency, amount in self.wallet.items():
            print(f"{currency}: {amount}")


# Money Display
money_system = MoneySystem()
money_system.add_money("USD", 1000)
money_system.check_balance()


while True:
    # Prompt the user to play or quit
    choice = input("[P]lay or [Q]uit: ")
    if choice == 'Q' or choice == 'q':
        break
    elif choice == 'P' or choice == 'p':
        print("Let's play!")

        # Define the deck of cards
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        deck = [(rank, suit) for rank in ranks for suit in suits]
        bj_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

        # Shuffle the deck
        random.shuffle(deck)

        # Deal hands to the player and dealer
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Remove the bet from the wallet
        money_system.remove_money("USD", 25)
        money_system.check_balance()

        # Display the hands
        print("Player's hand:", player_hand)
        print("Dealer's hand:", [dealer_hand[1]])

        # Player Hit
        while True:
            choice = input("[H]it or [S]tay: ")
            if choice == 'H' or choice == 'h':
                player_hand.append(deck.pop())
                if sum([bj_values[card[0]] for card in player_hand]) > 21:
                    print("Player's hand:", player_hand)
                    print("Dealer's hand:", [dealer_hand[1]])
                    print("You bust! Dealer wins.")
                    break
                else:
                    print("Player's hand:", player_hand)
                    print("Dealer's hand:", [dealer_hand[1]])
            elif choice == 'S' or choice == 's':
                print("Player's hand:", player_hand)
                print("Dealer's hand:", [dealer_hand[1]])
                break

        # Dealer Hit
        def dealer_hit(dealer_hand, deck):
            while sum([bj_values[card[0]] for card in dealer_hand]) < 17:
                dealer_hand.append(deck.pop())

        dealer_hit(dealer_hand, deck)

        # Display the final hands
        print("Player's hand:", player_hand)
        print("Dealer's hand:", dealer_hand)

        # Determine the winner
        player_sum = sum([bj_values[card[0]] for card in player_hand])
        dealer_sum = sum([bj_values[card[0]] for card in dealer_hand])

        if player_sum > 21:
            print("You bust! Dealer wins.")
            money_system.check_balance()
        elif dealer_sum > 21:
            print("Dealer busts! You win.")
            money_system.add_money("USD", 50)
            money_system.check_balance()
        elif player_sum > dealer_sum:
            print("You win!")
            money_system.add_money("USD", 50)
            money_system.check_balance()
        elif dealer_sum > player_sum:
            print("Dealer wins!")
            money_system.check_balance()
        else:
            print("Push.")
            money_system.check_balance()
            money_system.add_money("USD", 25)

