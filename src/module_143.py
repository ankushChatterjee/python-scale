"""Module 143: arithmetic helpers."""

def min_143(a, b):
    return a if a < b else b

def max_143(a, b):
    return a if a > b else b

def modulo_143(a, b):
    return a % b

def divide_143(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
