# -*- coding: utf-8 -*-
import os, sys, time, random

coin = lambda: random.choice((True, False))
val = lambda: random.randint(1, 15)

from operator import add, sub

def quickClr():
    os.system('clear')

correct, incorrect = (0, 0)
total = 10

def exercise(a, b, op):
    return '{} {} {} = '.format(a, op, b), {'+': add, '-': sub}[op](a, b)

args = set(sys.argv)

remaining = total
while remaining:
    remaining = remaining - 1
    if '--ls' not in args:
        quickClr()
    a, b = (val(), val())
    if '--prefer-sub' in args:
        substract = coin()
        negs = (substract, substract)
    else:
        negs = (coin(), coin())
    if a - b > 0 and negs[0]:
        expr, answer = exercise(a, b, '-')
    elif b - a > 0 and negs[1]:
        expr, answer = exercise(b, a, '-')
    else:
        if coin():
            expr, answer = exercise(a, b, '+')
        else:
            expr, answer = exercise(b, a, '+')
    if '--ls' not in args:
        cand = raw_input(expr)
        if int(cand) == answer:
            print('RÄTT')
            correct += 1
        else:
            print('FEL')
            incorrect += 1
        time.sleep(1)
    else:
        print(expr)

if '--ls' not in args:
    print('Färdigt. {} rätt, {} fel (av {})'.format(correct, incorrect, total))
