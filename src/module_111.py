"""Module 111: arithmetic helpers."""

def add_111(a, b):
    return a + b

def power_111(a, b):
    return a ** b

def subtract_111(a, b):
    return a - b

def divide_111(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
