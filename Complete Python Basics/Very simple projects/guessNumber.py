import random

def guessNumber():
    # Ask the person what number the system is guessing from 1-10
    print('Hey! If you guess the number between 1-10, I will give you a dollar!')
    randomNumber = random.randint(1,10)
    # this will only give 5 guesses 
    for i in range(1,6):
        print('Take a guess: ')
        x = int(input())
        if x == randomNumber:
            print('Congrats! I owe you a dollar.')
            break
        elif x < randomNumber:
            print('That is a little bit too low')
        elif x > randomNumber:
            print('That is a bit too high')
    print('Sorry! The nunmber I was thinking of is '+ str(randomNumber))

if __name__=="__main__":
    guessNumber()