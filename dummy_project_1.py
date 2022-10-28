from pywebio.input import *
from pywebio.output import *
import random
def make_shuffle(word):
    new_word = random.sample(word,k=len(word))
    new_word = ''.join(new_word)
    return new_word
def puzzle_words(score,word):
    new_word = make_shuffle(word)
    put_text("\nArrange the letters to form a valid words")
    put_text(new_word)
    user_word = input()
    if user_word.upper() == word:
        style(put_text("Correct"),'color:green')
        score+=1
    else:
        style(put_text("Wrong"),'color:red')
        score-=1
    return score
def main():
    score = 0
    words = ['FATHER','BREAK','COUNTRY','GREEN','AEROPLANE']
    words = random.sample(words,k=len(words))
    for word in words:
        score = puzzle_words(score,word)
    style(put_text("Net Score is ",score),'color:green')
main()
again = radio("Do you want to play again😍?",['Yes','No'])
if again == 'Yes':
    main()
else:
    put_text("Thanks for playing😁")