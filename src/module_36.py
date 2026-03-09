"""Module 36: arithmetic helpers."""

def subtract_36(a, b):
    return a - b

def multiply_36(a, b):
    return a * b

def divide_36(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_36(a, b):
    return a if a > b else b
