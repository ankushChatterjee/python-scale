"""Module 171: arithmetic helpers."""

def subtract_171(a, b):
    return a - b

def modulo_171(a, b):
    return a % b

def max_171(a, b):
    return a if a > b else b

def divide_171(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
