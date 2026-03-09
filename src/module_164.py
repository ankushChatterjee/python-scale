"""Module 164: arithmetic helpers."""

def divide_164(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_164(a, b):
    return a if a > b else b

def multiply_164(a, b):
    return a * b

def power_164(a, b):
    return a ** b
