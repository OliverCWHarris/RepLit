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
    if guess in word:
        word_count=word.count(guess)
        print("correct! ",guess," is in the word, ",word_count," times!")

        letter_position=word.index(guess)
        print("The letter: ",guess," is letter: ",letter_position+1)
        
        if word_count>=2:
            print("and in other places!")

        guesses2()

    elif guess==word:
        print("that is the word! well done!\nPlayer 1 wins!")
        quit

    else:
        print("sorry, ",guess," is not in the word")
        guesses2()


def guesses2():
    global guesses
    global number

    print("letters in word: ",word_length)
    guess=str(input("p2 enter guess\n: "))
    if guess in word:
        word_count=word.count(guess)
        print("correct! ",guess," is in the word, ",word_count," times!")

        letter_position=word.index(guess)
        print("The letter: ",guess," is letter: ",letter_position+1)
        
        if word_count>=2:
            print("and in other places!")
        
        guesses1()

    elif guess==word:
        print("that is the word! well done!\nPlayer 2 wins!")
        quit

    else:
        print("sorry, ",guess," is not in the word")
        guesses1()



main()