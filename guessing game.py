import random
import time
#definition of functions
def guess(x):
    guess = 0
    random_number = random.randint(1, x)
    while guess != random_number:
        guess = int(input(f'select a number from 1 to {x} : '))
        if guess < random_number:
            print('too low try again')
        elif guess > random_number:
            print('too high lets try again chap')

    print('you did it bozo!!\n')

guess(10)

time.sleep(3)
print('ready for round two?')
time.sleep(3)
print('whether you say yes or no')
time.sleep(2)
print('I\'TS MY TURN NOW')
time.sleep(2)
print('now,')
time.sleep(3)
print('ready')
time.sleep(2)
print('set')
time.sleep(1)
print('GOOOOOOOOOOOO!👾\n')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is {guess} (H) FOR HIGH, (L) FOR LOW, (C) FOR CORRECT GUESS: ').lower()
        if computer_guess == 'h':
            high-=guess
        elif feedback == 'l':
            low+=guess
    print(f'yay I THE COMPUTER guessed the number {guess} correctly')


computer_guess(10)
