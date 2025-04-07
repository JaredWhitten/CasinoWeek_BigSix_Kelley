# Jared Whitten ~ Big Six Game ~ Casino Week for Professor Kelley's class
import random
import time # adding this in so it makes it seem like the wheel takes a little bit to spin so the user feels like they are actually playing a game.

#function to show the rules of the game and the pay table
def displayRules():
    print("Welcome to the Big Six Wheel! Here are the rules: ")
    print("There are 54 spaces on the wheel, each one corresponds to a payout")
    print("There are 24 spaces markes \'One' which pay out 1:1")
    print("There are 15 spaces marked \'Two' which pay out 2:1")
    print("There are 7 spaces marked \'Five' which pay out 5:1")
    print("There are 4 spaces marked \'Ten' which pay out 10:1")
    print("There are 2 spaces marked \'Twenty' which pay out 20:1")
    print("Finally there are two different joker spaces, each paying out 40:1, though only if you bet on the correct one.")

#function to allow users to place bets, it is called in the play round function
def placeBet(balance):
    print("$$$$$$$$Place your bets!!!$$$$$$$$$")
    print("1: Bet on the wheel landing on a \'One' space")
    print("2: Bet on the wheel landing on a \'Two' space")
    print("3: Bet on the wheel landing on a \'Five' space")
    print("4: Bet on the wheel landing on a \'Ten' space")
    print("5: Bet on the wheel landing on a \'Twenty' space")
    print("6: Bet on the wheel landing on the \'Red Joker' space")
    print("7: Bet on the wheel landing on the \'Blue Joker' space")
    print("8: Quit the game")
    while True:
        choice = str(input("Enter your choice (1-8): ")).lower() #adding in the ability for a user to type out the word instead of just the number.
        if choice == "8" or choice == "eight": 
            betType = "quit"
            betAmount = 0
            return betType, betAmount, balance
        # error handling for players who cannot read
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "one", "two", "three", "four", "five", "six", "seven"]:
            print("Invalid choice. Please try again.")
            continue
        #assiging user choiice to a bet type so that it can be handled by the play round function
        if choice == "1" or choice == "one":
            betType = 1
        elif choice == "2" or choice == "two":
            betType = 2
        elif choice == "3" or choice == "three":
            betType = 5
        elif choice == "4" or choice == "four":
            betType = 10
        elif choice == "5" or choice == "five":
            betType = 20
        elif choice == "6" or choice == "six":
            betType = "Red Joker"
        elif choice == "7" or choice == "seven":
            betType = "Blue Joker"
        while True:
            try: # error handling to make sure people aren't betting with money they do not have
                if betType != 0:
                    print(f"You have ${balance} available")
                    betAmount = int(input("Please enter how much you would like to bet: $"))
                    if betAmount <=0 or betAmount > balance:
                        print(f"Invalid bet amount. You have ${balance} available and must bet more than 0.")
                        continue
                    balance -= betAmount
                    return betType, betAmount, balance
            except ValueError:
                print("Please enter a valid number")

#function to spin the wheel and assign the spin to the bet based on the odds provided at https://wizardofodds.com/games/big-six/
def spinWheel():
    spinResult = random.randint(1,54) # picks from 1 through 54
    if 1 <= spinResult <= 24: # 44.44% chance
        return 1
    elif 25 <= spinResult <= 39: # 27.78% chance
        return 2
    elif 40 <= spinResult <= 46: # 12.96% chance
        return 5
    elif 47 <= spinResult <= 50:  # 7.41% chance
        return 10
    elif 51 <= spinResult <= 52: # 3.70% chance
        return 20
    elif spinResult == 53: # 1.85% chance for each joker.
        return "Red Joker"
    else:
        return "Blue Joker"

# our function that plays the round, calls both our place bet function and our spin wheel function
def playRound(balance):
    betType, betAmount, balance = placeBet(balance)
    if betType == "quit":
        return balance, False
    print("Spinning the wheel!")
    time.sleep(0.8)
    print(".")
    time.sleep(0.8)
    print("..")
    time.sleep(0.8)
    print("...")
    time.sleep(1)
    result = spinWheel()
    print(f"The wheel has landed on a {result} symbol!")
    if result == betType:
        if result == "Red Joker" or result == "Blue Joker":  # if we landed on one of the jokers, pays out if you have the correct one.
            winnings = betAmount * 40
        else:
            winnings = betAmount * result
        balance += winnings + betAmount # have to re add the bet amount as well as the winnings in order to give the player back the money they bet and the money they won.
        print(f"Congratulations! You won ${winnings}! Your new balance is ${balance}")
    else:
        print("LOUD INCORRECT BUZZER SOUND (https://www.youtube.com/watch?v=EhkQxkZ0G1s)")
        print(f"Sorry, you lost ${betAmount} :( your new balance is ${balance}") #no need to remove money because we remove the bet amount in the place bet function
    if balance <= 0:
        print("You're out of money! Game over.")
        return balance, False
    elif balance > 0:     
        while True:
            try:
                playAgain = input("Would you like to play again? (y/n):").lower()
                if playAgain == "y" or playAgain == "yes":
                    return balance, True
                elif playAgain == "n" or playAgain == "no":
                    return balance, False
                else:
                    print("Please enter only yes or no.")
            except ValueError:
                print("Please enter only yes or no.")






# main function to start up game play as well as loop the game should the player wish to continue playing
def main():
    displayRules()
    while True: # while loops allows us to start the game over whenever the player leaves or loses.
        while True:
            try: #error handling to make sure the user is only entering whole dollar bills into the machine.
                balance = int(input("\nPlease enter how much money you would like to deposit into the machine: $"))
                if balance >= 0:
                    break
                else:
                    print("Please enter a non-negative number. This machine does not owe you money.")
            except ValueError:
                print("ERROR, please only enter a whole number into the machine")
        while balance > 0:
            balance, playAgain = playRound(balance)
            if not playAgain:
                break
        print(f"Thank you for playing, you ended with ${balance}")




    
main()
