#!/usr/bin/python

from agent import resolve

print resolve(['or', 'a', 'b', 'c', 'd', ['not', 'e'], ['not', 'f']], ['not', 'e'])
print resolve(['or', ['not', 'a'], ['not', 'b']], 'a')
print resolve('a', 'b')
print resolve(['or', 'a', 'b', 'c'], ['or', ['not', 'a'], ['not', 'b'], ['not', 'c']])
print resolve(['or', 'a', 'b', 'c'], ['or', ['not', 'b'], 'c'])
print resolve(['or', ['not', 'a'], 'b'], ['or', 'a', ['not', 'b']])
print resolve(['or', 'a', 'b', 'c', 'd', ['not', 'e']], ['or', 'd', 'e'])
print resolve(['or', 'a', 'b', 'c', 'd', ['not', 'e']], ['or', 'a', ['not', 'e']])