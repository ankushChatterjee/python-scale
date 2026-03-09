"""Module 39: arithmetic helpers."""

def divide_39(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_39(a, b):
    return a - b

def multiply_39(a, b):
    return a * b

def min_39(a, b):
    return a if a < b else b
