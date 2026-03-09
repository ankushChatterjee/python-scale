"""Module 165: arithmetic helpers."""

def min_165(a, b):
    return a if a < b else b

def multiply_165(a, b):
    return a * b

def divide_165(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_165(a, b):
    return a if a > b else b
