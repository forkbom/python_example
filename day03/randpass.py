from random import choice


all_chs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
