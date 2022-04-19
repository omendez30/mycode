from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

#function to set difficulty
def set_difficulty():
    difficulty = input('Choose a difficulty, \'easy\' or \'hard\': ')

    if difficulty == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

#Let user guess a number
def check_answer(guess, answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if guess > answer:
        print('Too High. \nGuess again.')
        
        return turns - 1
    elif guess < answer:
        print('Too low. \nGuess again.')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}')
   





def game():
    #choose a randome number between 1 and 100
    print('Guess the number i\'m thinking!')
    print('I\'m thinking of a number between 1 and 100: ')
    answer = randint(1,100)
    print(f'answer is {answer}')
    #determines the amount of attempts based off of difficulty
    turns = set_difficulty()
    
    #reapeat game functionality if the guess is wrong
    guess = 0
    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer,turns)
        
        if turns == 0:
            print('You ran out of guesses, you lose.')
            return exit


game()
