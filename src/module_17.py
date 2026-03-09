"""Module 17: arithmetic helpers."""

def min_17(a, b):
    return a if a < b else b

def multiply_17(a, b):
    return a * b

def divide_17(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_17(a, b):
    return a if a > b else b
