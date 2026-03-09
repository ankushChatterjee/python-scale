"""Module 159: arithmetic helpers."""

def multiply_159(a, b):
    return a * b

def min_159(a, b):
    return a if a < b else b

def divide_159(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_159(a, b):
    return a - b
