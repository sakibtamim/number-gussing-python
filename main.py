import random

guesses_list = []


def start_game():
    number = random.randint(1, 10)
    guesses = 0

    print('Hello! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')

    if wanna_play != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        pass

    while wanna_play == 'yes':
        try:
            guess = int(input("Enter Guess: "))

            guesses += 1
            guesses_list.append(guesses)

            if guess == number:
                print('Nice! You got it.')
                print(f'it took you {guesses} guesses')
                wanna_play = input(
                    f'Hi, {player_name}, would you like to play '
                    f'the guessing game? (Enter Yes/No): ')
                if wanna_play != 'yes':
                    print(f'That\'s cool, Thanks!')
                    break
                else:
                    guesses = 0
                    number = random.randint(1, 10)
                    continue

            else:
                if guess < number:
                    print("Guess higher!")
                elif guess > number:
                    print("Guess lower!")

        except ValueError:
            print('That is not a valid value. Try again...')


if __name__ == '__main__':
    start_game()
