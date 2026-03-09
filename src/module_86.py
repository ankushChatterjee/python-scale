"""Module 86: arithmetic helpers."""

def divide_86(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_86(a, b):
    return a * b

def min_86(a, b):
    return a if a < b else b

def subtract_86(a, b):
    return a - b
