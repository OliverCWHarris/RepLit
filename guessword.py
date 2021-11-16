import time
import os




def main():
    global guesses
    global word
    global word_length
    word=str(input("p3 enter word\n: "))
    word_length=len(word)
    os.system('cls')
    guesses1()


def guesses1():
    global guesses
    global number

    print("letters in word: ",word_length)
    guess=str(input("p1 enter guess\n: "))
    if guess==word:
        print("that is the word! well done!\nPlayer 1 wins!")
        quit

    elif guess in word:
        letter_position=word.index(guess)
        print("The letter: ",guess," is letter: ",letter_position+1)

        guesses2()
    else:
        print("sorry, ",guess," is not in the word")
        guesses2()


def guesses2():
    global guesses
    global number

    print("letters in word: ",word_length)
    guess=str(input("p2 enter guess\n: "))

    if guess==word:
        print("that is the word! well done!\nPlayer 2 wins!")
        quit

    elif guess in word:
        letter_position=word.index(guess)
        print("The letter: ",guess," is letter: ",letter_position+1)
        
        guesses1()

    else:
        print("sorry, ",guess," is not in the word")
        guesses1()



main()