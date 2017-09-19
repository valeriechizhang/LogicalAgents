#!/usr/bin/python

from agent import *

CLEAR()
TELL(['or', 'a', ['and', 'b', 'c'], 'd',
    ['and', 'e', 'f', ['or', 'm', 'n', ['and', 'p', 'q', ['or', 'z', 'x', ['and', 's', 'v']]]]], 'h', 'g'])
print ASK(['or', 'e', 'b', 'a', 'd', 'h', 'g'])

CLEAR()
TELL(['biconditional', ['or', 'a', ['and', 'c', 'd']], ['and', 'e', ['or', 'f', 'g']]])
print ASK(['or', 'e', ['not', 'a'], ['not', 'a']])
print ASK(['or', 'c', 'a', ['not', 'g'], ['not', 'e']])

CLEAR()
TELL(['implies', ['or', 'a', 'b'], ['and', 'c', 'd']])
TELL('c')
print ASK(['or', 'd', ['not', 'a']])
print ASK('a')
print ASK(['not', 'c'])
TELL(['or', 'a', 'b'])
print ASK(['and', 'c', 'd'])


CLEAR()
TELL(['implies', ['or', 'a', ['and', 'b', 'c', 'd'] ], 'b'])
TELL('a')
TELL(['or', 'c', 'd'])
print ASK('b')
print ASK('c')