"""Module 62: arithmetic helpers."""

def max_62(a, b):
    return a if a > b else b

def subtract_62(a, b):
    return a - b

def divide_62(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_62(a, b):
    return a if a < b else b
