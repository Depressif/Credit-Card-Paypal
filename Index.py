from random import *


def generator():
    numbers = '1234567890'
    lot = ''
    years = ''
    ccv = ''
    for i in range(7):
        lot += numbers[randint(0, 9)]

    if randint(0, 2) == 0:
        month = numbers[0]
        month += numbers[randint(0, 1)]
    else:
        month = numbers[9]
        month += numbers[randint(0, 8)]

    years += numbers[randint(0, 6)]

    for i in range(3):
        ccv += numbers[randint(0, 9)]
    # the bin is a discover bit it's the first str of the return you can change for other bin (master-card, visa ...)

    return '657368006' + lot + '|' + month + '|202' + years + '|' + ccv
print(generator())
