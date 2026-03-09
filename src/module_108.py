"""Module 108: arithmetic helpers."""

def min_108(a, b):
    return a if a < b else b

def max_108(a, b):
    return a if a > b else b

def add_108(a, b):
    return a + b

def divide_108(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
