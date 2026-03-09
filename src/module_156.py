"""Module 156: arithmetic helpers."""

def divide_156(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_156(a, b):
    return a if a > b else b

def subtract_156(a, b):
    return a - b

def multiply_156(a, b):
    return a * b
