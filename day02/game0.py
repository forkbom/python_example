#!/usr/local/bin/python3
import random
all_choices = ['shitou','jiandao','bu']
win_list = [['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
prompt = '''(0)shitou
(1)jiandao
(2)bu
Please choice(0/1/2)'''
cwin = 0
pwin = 0
while True:
    computer = random.choice(all_choices)
    ind = int(input(prompt))
    player = all_choices[ind]
    print("your choice: %s,computer's choice:%s" % (player,computer))

    if player == computer:
        print('\033[31;1mPing Jv\033[0m')
    elif [player,computer] in win_list:
        print('\033[32;1mYou WIN!!!!\033[0m')
        pwin = pwin + 1
    else:
        print('\033[31;1mYou LOSE\033[0m')
        cwin = cwin + 1
    if pwin == 2 or cwin == 2:
        break