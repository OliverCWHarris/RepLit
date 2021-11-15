import time
import os




def main():
    global guesses
    global word
    word=str(input("p3 enter word\n: "))
    word_length=len(word)
    os.system('cls')
    print(word_length)
    guesses1()


def guesses1():
    global guesses
    global number

    guess=str(input("p1 enter first guess\n: "))
    if guess in word:
        print("correct! ",guess," is in the word")
        guesses2()

    else:
        print("sorry, ",guess," is not in the word")
        guesses2()


def guesses2():
    global guesses
    global number
    guess=str(input("p2 enter first guess\n: "))
    if guess in word:
        print("correct! ",guess," is in the word")
        guesses1()

    else:
        print("sorry, ",guess," is not in the word")
        guesses1()



main()