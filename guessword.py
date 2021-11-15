import time
import os

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    global encrypted_word
    encrypted_word=word.replace("a","1")
    encrypted_word=word.replace("b","2")
    encrypted_word=word.replace("c","3")
    encrypted_word=word.replace("d","4")
    encrypted_word=word.replace("e","5")
    encrypted_word=word.replace("f","6")
    encrypted_word=word.replace("g","7")
    encrypted_word=word.replace("h","8")
    encrypted_word=word.replace("i","9")
    encrypted_word=word.replace("j","10")
    encrypted_word=word.replace("k","11")
    encrypted_word=word.replace("l","12")
    encrypted_word=word.replace("m","13")
    encrypted_word=word.replace("n","14")
    encrypted_word=word.replace("o","15")
    encrypted_word=word.replace("p","16")
    encrypted_word=word.replace("q","17")
    encrypted_word=word.replace("r","18")
    encrypted_word=word.replace("s","19")
    encrypted_word=word.replace("t","20")
    encrypted_word=word.replace("u","21")
    encrypted_word=word.replace("v","22")
    encrypted_word=word.replace("w","23")
    encrypted_word=word.replace("x","24")
    encrypted_word=word.replace("y","25")
    encrypted_word=word.replace("z","26")


def main():
    global guesses
    global word
    word=str(input("p3 enter word\n: "))
    word_length=len(word)
    guesses=word_length
    encrypt()
    os.system('cls')
    guesses1()

def guesses1():
    global guesses
    global number
    global encrypted_word
    guess=str(input("p1 enter first guess\n: "))
    if guess in word:
        print("correct! ",guess," is in the word")
        number=alphabet.index(guess)
        encrypted_word=word.replace("number",guess)
        guesses=guesses-1
        if 'guesses'==0:
            quit
        print(guesses)
        guesses2()
    else:
        print("sorry, ",guess," is not in the word")
        guesses=guesses-1
        if 'guesses'==0:
            quit
        print(guesses)
        guesses2()


def guesses2():
    global guesses
    global number
    guess=str(input("p2 enter first guess\n: "))
    if guess in word:
        print("correct! ",guess," is in the word")
        guesses=guesses-1
        if 'guesses'==0:
            quit
        print(guesses)
        guesses1()
    else:
        print("sorry, ",guess," is not in the word")
        guesses=guesses-1
        if 'guesses'==0:
            quit
        print(guesses)
        guesses1()



main()