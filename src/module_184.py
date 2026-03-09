"""Module 184: arithmetic helpers."""

def modulo_184(a, b):
    return a % b

def max_184(a, b):
    return a if a > b else b

def min_184(a, b):
    return a if a < b else b

def divide_184(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
