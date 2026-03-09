"""Module 109: arithmetic helpers."""

def divide_109(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_109(a, b):
    return a - b

def max_109(a, b):
    return a if a > b else b

def multiply_109(a, b):
    return a * b
