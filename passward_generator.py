import random
import string

def p_gen():
    n=int(input('enter the length of passward :- '))
    lette=input('digit y/n :-')
    digit=input('number y/n :-')
    speci=input('special character y/n :-')
    if lette=='n' and digit=='n' and speci=='n':
        print('please enter correct values')
        print(p_gen())
    else:
        a=''
        a +=string.ascii_letters if lette=='y' else ''
        a +=string.digits if digit=='y' else ''
        a +=string.punctuation if speci=='y' else ''
        ab=''.join(random.choices(a,k=n))
    return(ab)

print(p_gen())