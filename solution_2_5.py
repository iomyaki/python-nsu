def guess_the_number():
    from random import randint

    hidden = randint(1, 100)

    print('In this game, you have to guess a whole number from 1 to 100, both included')
    print('You can always type -1 to leave the game')
    attempts = 1
    while hidden:
        guess = int(input('Please, guess a number: '))
        if guess == hidden:
            return f'Congrats! The hidden number was {hidden}. You guessed right on the {attempts} try'
        elif guess == -1:
            return (f'The game is over. You have made {attempts - 1} ' +
                    ('attempt' if attempts == 2 else 'attempts') + ' before leaving')
        else:
            print(f'The hidden number is ' + ('BIGGER' if guess < hidden else 'SMALLER') + ' than you now guessed')
        attempts += 1


print(guess_the_number())
