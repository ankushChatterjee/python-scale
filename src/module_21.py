"""Module 21: arithmetic helpers."""

def multiply_21(a, b):
    return a * b

def divide_21(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_21(a, b):
    return a if a < b else b

def max_21(a, b):
    return a if a > b else b
