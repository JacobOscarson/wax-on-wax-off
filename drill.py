# -*- coding: utf-8 -*-
from itertools import count, combinations, islice, izip

import time, random

reaching = lambda n: islice(count(1), n)
coin = lambda: random.choice((True, False))
val = lambda: random.randint(1, 15)

def quickClr():
    print(chr(27) + "[2J")

correct, incorrect = (0, 0)
total = 10

n = total
while n:
    quickClr()
    a, b = (val(), val())
    if coin():
        minus = coin()
        if a - b > 0 and coin():
            expr = '{} - {} = '.format(a,b)
            answer = a - b
            n -= 1
        elif b - a > 0 and coin():
            expr = '{} - {} = '.format(b, a)
            answer = b - a
            n -= 1
        else:
            expr = '{} + {} = '.format(a,b)
            answer = a + b
            n -= 1
        cand = raw_input(expr)
        if int(cand) == answer:
            print('RÄTT')
            correct += 1
        else:
            print('FEL')
            incorrect += 1
        time.sleep(1)

print('Färdigt. {} rätt, {} fel (av {})'.format(correct, incorrect, total))
