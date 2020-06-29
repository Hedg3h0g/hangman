import random

print("H A N G M A N")
while True:
    print("Type \"play\" to play the game, \"exit\" to quit: ")
    x = input()
    if x == "play":
        lives = 8
        variants = ['python', 'java', 'kotlin', 'javascript']
        rand_word = list(random.choice(variants))
        wrong = set()
        hint = list("-" * len(rand_word))

        while lives > 0:
            print()
            for x in hint:
                print(x, end="")
            print()
            if hint == rand_word:
                print("You guessed the word!")
                break
            else:
                print("Input a letter: ", end="")
                char = input()

            if len(char) > 1:
                print("You should input a single letter")
            elif char.isupper() or not (char.isalpha()):
                print("It is not an ASCII lowercase letter")
            elif char in set(wrong):
                print("You already typed this letter")
            elif char in rand_word:
                for x in range(len(rand_word)):
                    if rand_word[x] == char:
                        hint[x] = char
                        wrong.add(char)
            else:
                lives -= 1
                print("No such letter in the word")
                wrong.add(char)

        if lives == 0:
            print("You are hanged!")
            print()
        else:
            print("You survived!")
            print()

    elif x == "exit":
        break
    else:
        continue
