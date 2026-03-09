"""Module 151: arithmetic helpers."""

def subtract_151(a, b):
    return a - b

def divide_151(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_151(a, b):
    return a if a < b else b

def multiply_151(a, b):
    return a * b
