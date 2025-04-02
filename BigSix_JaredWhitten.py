import random

def displayRules():
    print("============================")
    print("Welcome to the Big Six Wheel! Here are the rules:")
    print("The wheel has 54 spaces, each corresponding to a specific payout")
    print("- 24 spaces with 1:1 payout")
    print("- 15 spaces with 2:1 payout")
    print("- 7 spaces with 5:1 payout")
    print("- 4 spaces with 10:1 payout")
    print("- 2 spaces with 20:1 payout")
    print("- 1 Joker 1 space (40:1 payout)")
    print("- 1 Joker 2 space (40:1 payout)")
    print("============================")

def spinWheel():
    spinResult = random.randint(1, 54)
    if 1 <= spinResult <= 24:
        return 1
    elif 25 <= spinResult <= 39:
        return 2
    elif 40 <= spinResult <= 46:
        return 5
    elif 47 <= spinResult <= 50:
        return 10
    elif 51 <= spinResult <= 52:
        return 20
    elif spinResult == 53:
        return "Joker 1"
    else:
        return "Joker 2"

def placeBet(balance):
    print("What would you like to bet on?")
    print("1: Bet on 1")
    print("2: Bet on 2")
    print("3: Bet on 5")
    print("4: Bet on 10")
    print("5: Bet on 20")
    print("6: Bet on Joker 1")
    print("7: Bet on Joker 2")
    print("8: Quit game")
    
    while True:
        choice = input("Enter your choice (1-8): ")
        
        if choice == "8":
            print("Thanks for playing! Come back again soon!")
            return None, 0
        
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == "1":
            betType = 1
        elif choice == "2":
            betType = 2
        elif choice == "3":
            betType = 5
        elif choice == "4":
            betType = 10
        elif choice == "5":
            betType = 20
        elif choice == "6":
            betType = "Joker 1"
        elif choice == "7":
            betType = "Joker 2"
        
        try:
            betAmount = int(input(f"How much would you like to bet? (1-{balance}): $"))
            if betAmount <= 0 or betAmount > balance:
                print(f"Invalid bet amount. You have ${balance} available.")
                continue
            return betType, betAmount
        except ValueError:
            print("Please enter a valid number.")

def playRound(balance, totalWins, totalLosses, totalSpins):
    """Play a single round of the game and return updated stats"""
    # Display current stats
    print(f"\nYour current balance: ${balance}")
    print(f"Total spins: {totalSpins}, Wins: {totalWins}, Losses: {totalLosses}")
    
    betType, betAmount = placeBet(balance)
    
    if betType is None:
        return balance, totalWins, totalLosses, totalSpins, False
    
    totalSpins += 1
    print("\nSpinning the wheel...")
    result = spinWheel()
    print(f"The wheel landed on: {result}")
    
    if result == betType:
        if isinstance(result, int):
            winnings = betAmount * result
        else:  
            winnings = betAmount * 40
        
        balance += winnings
        totalWins += 1
        print(f"Congratulations! You won ${winnings}!")
    else:
        balance -= betAmount
        totalLosses += 1
        print(f"Sorry, you lost ${betAmount}.")
    
    if balance <= 0:
        print("You're out of money! Game over.")
        return balance, totalWins, totalLosses, totalSpins, False

    
    playAgain = input("\nWould you like to play again? (yes/no): ").lower()
    continuePlaying = playAgain == "yes" or playAgain == "y"
    
    if not continuePlaying:
        print(f"Thanks for playing! You're leaving with ${balance}.")
        print(f"Final stats - Spins: {totalSpins}, Wins: {totalWins}, Losses: {totalLosses}")
    
    return balance, totalWins, totalLosses, totalSpins, continuePlaying

def main():
    displayRules()
    
    balance = 100
    totalWins = 0
    totalLosses = 0
    totalSpins = 0
    playing = True
    
    while playing:
        balance, totalWins, totalLosses, totalSpins, playing = playRound(
            balance, totalWins, totalLosses, totalSpins
        )
        
main()
































