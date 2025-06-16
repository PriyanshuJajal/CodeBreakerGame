import random

def generateSecretCode():
    """
    Generates a random 4-digit secret code as a list of strings.
    """
    secretCode = []
    for _ in range(4):
        digit = str(random.randint(0, 9))
        secretCode.append(digit)
    return secretCode

def calcFeedback(secretCode, playerGuess):
    """
    Calculates the number of bulls and cows for a given guess.
    """
    bulls = 0
    cows = 0

    secretCodeCopy = list(secretCode)
    playerGuessCopy = list(playerGuess)

    # Calculate Bulls
    for i in range(len(secretCodeCopy) - 1, -1, -1):
        if secretCodeCopy[i] == playerGuessCopy[i]:
            bulls += 1
            secretCodeCopy.pop(i)
            playerGuessCopy.pop(i)

    # Calculate Cows
    for i in range(len(playerGuessCopy) - 1, -1, -1):
        if playerGuessCopy[i] in secretCodeCopy:
            cows += 1
            secretCodeCopy.remove(playerGuessCopy[i])

    return bulls, cows