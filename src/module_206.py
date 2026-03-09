"""Module 206: arithmetic helpers."""

def divide_206(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_206(a, b):
    return a * b

def subtract_206(a, b):
    return a - b

def min_206(a, b):
    return a if a < b else b
