# Imports
from wonderwords import RandomWord
import time
# Set variables
lives = 0
randomword = []
word = ""
userguess = []
correct = set()  # Store unique guessed letters
lose = False

# Define functions
def generateword():
    global word, randomword
    rw = RandomWord()
    word = rw.word(word_min_length=4, word_max_length=8).lower()
    randomword = list(word)
    return word

def takeinput(): 
    while True:   
        uinput = input("Enter guess: ").replace(" ", "").lower()
        if uinput:
            return uinput
        print("You gotta say something")

def checkinput1(userguess):
    global lives, correct
    if len(userguess) == 1:  # Single letter guess
        if userguess in randomword:
            print(userguess, "is correct!")
            correct.add(userguess)  # Store unique letters only
        else:
            print(userguess, "is not in the word")
            lives -= 1
    elif userguess == word:  # Full word guess
        print("You got it!", word, "was the word.")
        return True
    else:
        print("Incorrect guess")
        lives -= 1

    # Check if all unique letters have been guessed
    if set(randomword) == correct:
        print("Congratulations! You guessed all letters. The word was:", word)
        return True

    return False

def displayprogress():
    progress = "".join([letter if letter in correct else "_" for letter in randomword])
    print(f"Word: {progress}")
    return progress

# Start game
print("welcome to hackman! play like normal hangman and have fun!")
time.sleep(0.2)
generateword()
uans2 = input("Do you want to set a custom amount of lives? | yes/no ").lower()
if 'yes' in uans2:
    uans3 = int(input("How many lives do you want? | (insert number) "))
    time.sleep(0.2)
    lives = uans3
else:
    lives = 7
    time.sleep(0.2)

# Game Loop
while lives > 0:  # Only continue if lives are above 0
    print("Lives =", lives)
    time.sleep(0.2)
    displayprogress()
    time.sleep(0.2)
    userguess = takeinput()
    time.sleep(0.2)
    if checkinput1(userguess):
        uans4 = input("do you want to play again? | yes/no ").lower()
        if 'yes' in uans4:
            correct = []
            print("you think you can win again? good luck!")
            time.sleep(0.2)
            generateword()
            uans2 = input("Do you want to set a custom amount of lives? | yes/no ").lower()
            if 'yes' in uans2:
                uans3 = int(input("How many lives do you want? | (insert number) "))
                time.sleep(0.2)
                lives = uans3
            else:
                lives = 7
                time.sleep(0.2)
        else:
            print("bye!")
            break
    if lives <= 0:  # Check if player has lost
        time.sleep(0.2)
        print("You Lose :(")
        time.sleep(0.2)
        print("The word was:", word)
        uans4 = input("do you want to play again? | yes/no ").lower()
        if 'yes' in uans4:
            correct = []
            print("you'll get it this time! ")
            time.sleep(0.2)
            generateword()
            uans2 = input("Do you want to set a custom amount of lives? | yes/no ").lower()
            if 'yes' in uans2:
                uans3 = int(input("How many lives do you want? | (insert number) "))
                time.sleep(0.2)
                lives = uans3
            else:
                lives = 7
                time.sleep(0.2)
        else:
            print("bye!")
            break