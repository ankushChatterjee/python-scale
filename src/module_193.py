"""Module 193: arithmetic helpers."""

def divide_193(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_193(a, b):
    return a ** b

def max_193(a, b):
    return a if a > b else b

def min_193(a, b):
    return a if a < b else b
