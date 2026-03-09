"""Module 77: arithmetic helpers."""

def divide_77(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_77(a, b):
    return a if a > b else b

def add_77(a, b):
    return a + b

def modulo_77(a, b):
    return a % b
