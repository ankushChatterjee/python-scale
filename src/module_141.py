"""Module 141: arithmetic helpers."""

def subtract_141(a, b):
    return a - b

def divide_141(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_141(a, b):
    return a if a > b else b

def min_141(a, b):
    return a if a < b else b
