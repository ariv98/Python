import random
def chc(c):
    if c == 0:
        print(f'You have {c} guess left️')
        print("\n\n\t\tGAME OVER\nThank you for playing\n\n")
    elif c == 1:
        print(f'You have only {c} guess left, Be carefull')
    elif c == 2:
        print(f'\nYou have {c} guesses left')
s = input(("\nShall we start the game (y/n): "))
chance = 3
count = 0
if s == 'y':
    print("\nYou have 3 chances")
    while count < 3:
        r = random.randint(1, 10)
        a = int(input("\nGuess the number between 1 to 10: "))
        if a == 0 or a > 10:
            print("\n❗❗❗The guessing number should be between 1 to 10 and not 0❗❗❗")
            chance -= 1
            chc(chance)
        elif a != r:
            print("\t❗❗❗WRONG GUESS❗❗❗")
            print(f'The correct guess is {r}')
            chance -= 1
            chc(chance)
        elif a == r:
            print("\n\n\t\tWOW!!!Correct guess")
            print("\t\tCongratulations you won the game")
            break
        count += 1
elif s != 'y' and s != 'n':
    print("\nPlease select the correct input")
elif s == 'n':
    print("\nGet lost hehehe")