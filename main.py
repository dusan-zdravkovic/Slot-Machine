def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


MAX_LINES = 3


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")


def get_bet(balance, lines):
    while True:
        bet = input(f"How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            total_bet = bet * lines
            if bet > 0 and total_bet <= balance:
                return bet
            elif total_bet > balance:
                print(f"Total bet (${total_bet}) exceeds your balance (${balance}).")
            else:
                print("Bet must be greater than 0.")
        else:
            print("Please enter a valid number.")


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet(balance, lines)
        total_bet = bet * lines

        print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

        # Placeholder for spinning the slot machine and updating balance
        # balance += winnings - total_bet

        play_again = input("Press enter to play again (q to quit): ")
        if play_again.lower() == "q":
            break

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
