import random
correct_answer = random.randint(1, 100)
guess = int(input('Guess a number between 1 and 100! '))
guesses = set()
repeated_guesses = 0
while guess != correct_answer:
    if (guess in guesses) == True:
        repeated_guesses += 1
        print('You have already guessed {}!'.format(guess))
        guess = int(input('Guess again: '))
        continue
    guesses.add(guess)
    if guess < correct_answer:
        print('Wrong! Your guess was too small.')   
    elif guess > correct_answer:
        print('Wrong! Your guess was too large.')
    guess = int(input('Guess again: '))

if guess == correct_answer:
    print('You Won! {} is the secret number. You guessed it in {} guesses.'.format(correct_answer, len(guesses)+repeated_guesses+1))


