"""Module 129: arithmetic helpers."""

def power_129(a, b):
    return a ** b

def divide_129(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_129(a, b):
    return a if a < b else b

def max_129(a, b):
    return a if a > b else b
