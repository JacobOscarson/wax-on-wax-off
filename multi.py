# -*- coding: utf-8 -*-
import os, sys, time, random
from string import digits

coin = lambda: random.choice((True, False))
val = lambda a,b: random.randint(a, b)

from operator import mul, div

def quickClr():
    sys.stderr.write("\x1b[2J\x1b[H")

correct, incorrect = (0, 0)
total = 10

def exercise(a, b, op):
    return '{} {} {} = '.format(a, op, b), {'*': mul, '/': div}[op](a, b)

args = set(sys.argv)

def say_wrong(expr, answer):
    print('\nFEL, {} {}'.format(expr, answer))
    time.sleep(1)

remaining = total
while remaining:
    remaining = remaining - 1
    if '--ls' not in args:
        quickClr()
    a, b = (random.choice((1,2,5,10)), random.choice(range(10)))
    if '--prefer-div' in args:
        divide = coin()
        divides = (divide, divide)
    else:
        divides = (coin(), coin())
    if divmod(b, a)[1] == 0 and divides[0]:
        expr, answer = exercise(b, a, '/')
    else:
        expr, answer = coin() and exercise(a, b, '*') or exercise(b, a, '*')
    if '--ls' not in args:
        cand = ''.join(ch for ch in raw_input(expr) if ch in digits)
        try:
            if int(cand) == answer:
                print('RÄTT')
                correct += 1
            else:
                incorrect += 1
                say_wrong(expr, answer)
        except ValueError:
            incorrect += 1
            say_wrong(expr, answer)

        time.sleep(1)
    else:
        print(expr)

if '--ls' not in args:
    print('Färdigt. {} rätt, {} fel (av {})'.format(correct, incorrect, total))
