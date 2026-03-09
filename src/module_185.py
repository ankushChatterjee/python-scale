"""Module 185: arithmetic helpers."""

def max_185(a, b):
    return a if a > b else b

def divide_185(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_185(a, b):
    return a ** b

def modulo_185(a, b):
    return a % b
