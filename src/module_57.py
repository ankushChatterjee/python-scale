"""Module 57: arithmetic helpers."""

def divide_57(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_57(a, b):
    return a + b

def min_57(a, b):
    return a if a < b else b

def max_57(a, b):
    return a if a > b else b
