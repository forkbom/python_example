import random

number = random.randint(1,100)
counter = 0

while counter < 5:
    guess = int(input('0-100:'))
    counter += 1
    if guess < number:
        print('Xiao Xiao')
    elif guess > number:
        print('DA DA DA')
    else:
        print('Conratulation')
        break
else:
    print('Number is %s'%number)
