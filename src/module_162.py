"""Module 162: arithmetic helpers."""

def multiply_162(a, b):
    return a * b

def min_162(a, b):
    return a if a < b else b

def divide_162(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_162(a, b):
    return a - b
