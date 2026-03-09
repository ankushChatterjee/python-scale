"""Module 158: arithmetic helpers."""

def power_158(a, b):
    return a ** b

def max_158(a, b):
    return a if a > b else b

def min_158(a, b):
    return a if a < b else b

def divide_158(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
