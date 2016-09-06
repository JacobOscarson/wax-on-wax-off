# -*- coding: utf-8 -*-
import os, sys, time, random
from string import digits

coin = lambda: random.choice((True, False))
val = lambda: random.randint(1, 15)

from operator import add, sub

def quickClr():
    sys.stderr.write("\x1b[2J\x1b[H")

correct, incorrect = (0, 0)
total = 10

def exercise(a, b, op):
    return '{} {} {} = '.format(a, op, b), {'+': add, '-': sub}[op](a, b)

args = set(sys.argv)

def say_wrong(expr, answer):
    print('\nFEL, {} {}'.format(expr, answer))
    time.sleep(1)

remaining = total
while remaining:
    remaining = remaining - 1
    if '--ls' not in args:
        quickClr()
    a, b = (val(), val())
    if '--prefer-sub' in args:
        subtract = coin()
        negs = (subtract, subtract)
    else:
        negs = (coin(), coin())
    if a - b > 0 and negs[0]:
        expr, answer = exercise(a, b, '-')
    elif b - a > 0 and negs[1]:
        expr, answer = exercise(b, a, '-')
    else:
        expr, answer = coin() and exercise(a, b, '+') or exercise(b, a, '+')
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
