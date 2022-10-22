import random


def guess(x):
    guess = 0
    random_number = random.randint(1, x)
    while guess != random_number:
        guess = int(input(f'select a number from 1 to {x} : '))
        if guess < random_number:
            print('too low try again')
        elif guess > random_number:
            print('too high lets try again chap')

    print('you did it bozo!!')


guess(10)
