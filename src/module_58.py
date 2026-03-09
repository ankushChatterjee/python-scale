"""Module 58: arithmetic helpers."""

def power_58(a, b):
    return a ** b

def divide_58(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_58(a, b):
    return a if a < b else b

def max_58(a, b):
    return a if a > b else b
