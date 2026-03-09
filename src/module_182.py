"""Module 182: arithmetic helpers."""

def subtract_182(a, b):
    return a - b

def divide_182(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_182(a, b):
    return a * b

def min_182(a, b):
    return a if a < b else b
