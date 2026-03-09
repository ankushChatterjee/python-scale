"""Module 154: arithmetic helpers."""

def min_154(a, b):
    return a if a < b else b

def divide_154(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_154(a, b):
    return a + b

def multiply_154(a, b):
    return a * b
