import random
STEPS = 5
START_NUMBER = 1
END_NUMBER = 20
def start_game():
    answer = random.randint(START_NUMBER, END_NUMBER) # this returns a random number between 1 and 20 (both inclusive)
    while True:
        print('What\'s your name?')
        name = input()
        if len(name) > 0:
            break
    print('\nHello, ' + name)
    print('I am thinking of a number between 1 and 20.\nCan you guess it within 5 steps?')
    for step in range(STEPS):
        while True:
            print('Take a guess (step ' + str(step + 1) + ' of ' + str(STEPS) + ')')
            guess = input()
            try:
                guess = int(guess)
            except ValueError:
                print('please input a number')
                continue
            if guess > END_NUMBER:
                print('The number cannot be greater than ' + str(END_NUMBER))
            elif guess < START_NUMBER:
                print('The number cannot be smaller than ' + str(START_NUMBER))
            else:
                break
        if guess < answer:
            print('The number is smaller than the answer')
        elif guess > answer:
            print('The number is greater than the answer')
        else:
            print('You\'ve guessed it! The answer is indeed ' + str(answer) + '!!!')
            print('You won the game in ' + str(step + 1) + ' steps!')
            return
    print('\nUnfortunately you have lost.\nThe answer is ' + str(answer))
start_game()
