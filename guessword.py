import time
import os


word=str(input("p1 enter word\n: "))
for i in word:
    encripted_word=word[:i]+'*'+word[i+1:]
os.system('cls')
guess1=str(input("p2 enter first guess\n: "))
if guess1 in word:
    print("correct! ",guess1," is in the word")
    print(encripted_word)
else:
    print("sorry, ",guess1," is npt in the word")
