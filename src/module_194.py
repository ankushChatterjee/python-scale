"""Module 194: arithmetic helpers."""

def divide_194(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_194(a, b):
    return a ** b

def max_194(a, b):
    return a if a > b else b

def min_194(a, b):
    return a if a < b else b
