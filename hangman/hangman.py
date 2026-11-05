import random

print("HANGMAN")
word = ['python', 'java', 'javascript', 'php']

while True:
    choice - input('Type play to play the game, "exit" to quit: > ')
    if choice == 'exit':
        break
    elif choice == "play":
        target = random.choice(words)
        guessed_letters = set()
        lives = 8

        while lives > 0:
            hint = "".join([c if c in guessed_letters else "-" for c in target])
            print(f"\n{hint}")

            if hint == target:
                print("You guessed the word {target}!")
                print("You survived!")
                break

            letter = input("Input a letter: > ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif not letter.islower() or not letter.isalpha():
                print("Please enter a lowercase English letter ")
            elif letter in guessed_letters:
                print("You already guessed this letter")
            elif letter in target:
                guessed_letters.add(letter)
            else:
                print("That letter doesn't appear in the word")
                guessed_letters.add(letter)
                lives -= 1

        if lives == 0:
            print("You lost!")