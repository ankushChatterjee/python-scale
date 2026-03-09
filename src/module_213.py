"""Module 213: arithmetic helpers."""

def max_213(a, b):
    return a if a > b else b

def add_213(a, b):
    return a + b

def min_213(a, b):
    return a if a < b else b

def divide_213(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
