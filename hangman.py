import random
import pyttsx3
import words
# setup the word and hidden list
attempts = 0
max_attempts = 4
word = words.words.random.choice(words)
hidden = []

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


for character in word:
    hidden.append('_')

# loop until the player has won or lost
isGameOver = False
while not isGameOver:

    #display current board, guessed letters, and attempts remaining
    print(f'you have {attempts} attempts left')

    hiddenString = ' '.join(hidden)
    print(f'The current letter is: {hiddenString}')
    
    print('     -----')
    print('     |   |')
    print('     |   '+ ('O' if attempts > 0 else ''))
    print('     |   '+ ('/\\' if attempts > 1 else ''))
    print('     |   '+ ('|' if attempts > 2 else ''))
    print('     |   '+ ('/\\' if attempts > 3 else ''))
    print('--------')

    
    # ask player for character
    letterGuessed = input("Please enter a letter: ")

    if letterGuessed in word:
        print(f'You guessed correctly! {letterGuessed} is in the word')
        for i in range(len(word)):
            character = word[i]
            if character in letterGuessed:
                hidden[i] = word[i]
                word[i] = '_'
    else:
        print(f'You guessed wrong! {letterGuessed} is NOT in the word')
        attempts += 1

    # if the player has won print a win message and stop looping
    if all('_' == char for char in word):
        print('Congratulations, you won')
        speak('Congratulations, you won')
        isGameOver = True

    # if the player has lost print a you lose message and stop looping
    if attempts >= max_attempts:
        print('You lost, rest in peace')
        speak('You lost, rest in peace')
        isGameOver = True