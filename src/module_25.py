"""Module 25: arithmetic helpers."""

def power_25(a, b):
    return a ** b

def subtract_25(a, b):
    return a - b

def max_25(a, b):
    return a if a > b else b

def divide_25(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
