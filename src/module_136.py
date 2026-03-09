"""Module 136: arithmetic helpers."""

def divide_136(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_136(a, b):
    return a ** b

def min_136(a, b):
    return a if a < b else b

def max_136(a, b):
    return a if a > b else b
