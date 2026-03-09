"""Module 138: arithmetic helpers."""

def add_138(a, b):
    return a + b

def min_138(a, b):
    return a if a < b else b

def max_138(a, b):
    return a if a > b else b

def divide_138(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
