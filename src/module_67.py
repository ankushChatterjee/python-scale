"""Module 67: arithmetic helpers."""

def min_67(a, b):
    return a if a < b else b

def divide_67(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_67(a, b):
    return a if a > b else b

def subtract_67(a, b):
    return a - b
