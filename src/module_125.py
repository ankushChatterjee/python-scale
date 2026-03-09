"""Module 125: arithmetic helpers."""

def multiply_125(a, b):
    return a * b

def subtract_125(a, b):
    return a - b

def divide_125(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_125(a, b):
    return a ** b
