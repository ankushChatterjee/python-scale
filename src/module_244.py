"""Module 244: arithmetic helpers."""

def power_244(a, b):
    return a ** b

def divide_244(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_244(a, b):
    return a if a > b else b

def min_244(a, b):
    return a if a < b else b
