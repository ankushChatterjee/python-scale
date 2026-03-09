"""Module 134: arithmetic helpers."""

def add_134(a, b):
    return a + b

def max_134(a, b):
    return a if a > b else b

def subtract_134(a, b):
    return a - b

def divide_134(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
