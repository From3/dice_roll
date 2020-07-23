import random
import time
from datetime import date

history = []
ps = ['Isridentas kauliukas: ', 'Isridenti kauliukai: ']


def adt(word):
    history.append(str(date.today()) + ' ' + str(time.strftime("%H:%M:%S")) + '\t\t' + str(word))


adt('Prisijungta')
print('Norint pamatyti kauliuku ridenimo istorija, prasant ridenti viena kauliuka, ivesti "h"')
while True:
    try:
        sides = input('\nJei ridenamas daugiau nei vienas kauliukas, ivesti "0"\nSieneliu skaicius: ')
        if sides == 'h' or sides == 'H':
            print('')
            for j in history:
                print(j)
        if int(sides) == 0:
            amount = input('\nJei ridenamas vienas kauliukas, ivesti "0"\nKauliuku skaicius (1 - 26): ')
            if int(amount) > 26:
                amount = 26
            elif int(amount) == 0:
                continue
            sides = input('Sieneliu skaicius: ')
            result = []
            for sk in range(int(amount)):
                result.append(str(random.randrange(1, int(sides) + 1)))
            multi_result = ", ".join(result)
            adt(multi_result)
            if int(amount) > 1:
                print(ps[1] + multi_result)
            else:
                print(ps[0] + multi_result)
        elif int(sides) > 0:
            result = random.randrange(1, int(sides) + 1)
            adt(result)
            print(ps[0] + str(result))
        else:
            continue
    except ValueError:
        continue
