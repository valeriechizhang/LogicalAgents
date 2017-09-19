#!/usr/bin/python

from agent import *

CLEAR()
print ASK('a')

CLEAR()
TELL('a')
TELL('b')
TELL('c')
TELL('d')
print ASK(['or', 'a', 'b', 'c', 'd'])


CLEAR()
TELL('a')
TELL('b')
TELL(['or', ['not', 'a'], 'b'])
TELL(['or', 'c', 'd'])
TELL('d')
print ASK(['or', 'b', 'd'])

CLEAR()
TELL(['or', 'a', 'b', 'c', 'd'])
TELL(['or', ['not', 'a'], 'b', 'c', 'd'])
TELL(['or', 'a', ['not', 'b'], 'c', 'd'])
TELL(['or', 'a', 'b', ['not', 'c'], 'd'])
TELL(['or', 'a', 'b', 'c', ['not', 'd']])
print ASK(['or', 'b', 'c'])
TELL(['not', 'a'])
print ASK(['or', 'b', 'c'])
TELL('b')
print ASK(['or', 'c', 'd'])

CLEAR()
TELL(['or', 'a', 'b', 'c'])
TELL(['or', ['not', 'b'], 'c', 'd'])
TELL(['or', ['not', 'c'], 'd', 'e'])
TELL(['or', ['not', 'd'], 'e', 'f'])
TELL(['not', 'e'])
TELL(['not', 'f'])
print ASK(['not', 'd'])
print ASK(['not', 'c'])
print ASK(['not', 'b'])
print ASK(['not', 'a'])














