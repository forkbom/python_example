#!/usr/local/bin/python3
import random
computer = (random.choice(['shitou','jiandao','bu']))
player = input('shitou/jiandao/bu:')

# print(computer,player)
if computer == player:
    print('Ping Ju')
elif computer == 'shitou' and player == 'jiandao':
    print('computer is ',computer,'you lose')
elif computer == 'shitou' and player == 'bu':
    print('computer is ',computer,'you win')

elif computer == 'bu' and player == 'jiandao':
    print('computer is ',computer,'you win')
elif computer == 'bu' and player == 'shitou':
    print('computer is ',computer,'you lose')

elif computer == 'jiandao' and player == 'shitou':
    print('computer is ',computer,'you win')
elif computer == 'jiandao' and player == 'bu':
    print('computer is ',computer,'you lose')
else:
    print('input error play again')