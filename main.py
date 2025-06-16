from game_logic import generateSecretCode , calcFeedback 

CODE_LENGTH = 4  
MAX_ATTEMPTS = 10

POSSIBLE_DIGITS = [str(i) for i in range(10)]  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def getPlayerGuess(attemptNum):
    
    while True:
        guessStr = input(f"Attempt {attemptNum}/{MAX_ATTEMPTS} - Enter your {CODE_LENGTH}-digit guess: ")

        if len(guessStr) != CODE_LENGTH:
            print(f"Invalid input. Please enter exactly {CODE_LENGTH} digits.")
            continue
        
        if not guessStr.isdigit():
            print("Invalid input. Please enter only digits.")
            continue
        
        # check if all digits are within POSSIBLE_DIGITS
        validDigits = True
        
        for digit in guessStr:
            if digit not in POSSIBLE_DIGITS:
                print(f"Invalid digit: '{digit}'. Only use digits from {POSSIBLE_DIGITS[0]}-{POSSIBLE_DIGITS[-1]}.")
                
                validDigits = False
                break
        if not validDigits:
            continue

        return list(guessStr) # Convert the string guess to a list of characters

def play_game():
    """Main function to run the Code Breaker game."""
    
    print("Welcome to Code Breaker!")
    print(f"Guess the 4 digit code in {MAX_ATTEMPTS} attempts or fewer.")
    print("Digits range from '0' to '9'. Duplicates are allowed")

    secretCode = generateSecretCode()

    attemptsTaken = 0
    
    while attemptsTaken < MAX_ATTEMPTS :
        attemptsTaken += 1
        print(f"\n --- Attempt {attemptsTaken} of {MAX_ATTEMPTS} --- ")

        playerGuess = getPlayerGuess(attemptsTaken)

        bulls , cows = calcFeedback(secretCode , playerGuess)

        print(f"Feedback: Bulls: {bulls} , Cows: {cows}")

        if bulls == CODE_LENGTH :
            print(f"\n Congratulations! You've cracked the code '{''.join(secretCode)}' in {attemptsTaken} attempts!")
            return

    # If loop finishes, player ran out of attempts
    print(f"Game Over! You ran out of attempts.")
    print(f"The secret code was: {''.join(secretCode)}")

if __name__ == "__main__":
    play_game()
    