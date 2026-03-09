"""Module 43: arithmetic helpers."""

def subtract_43(a, b):
    return a - b

def add_43(a, b):
    return a + b

def power_43(a, b):
    return a ** b

def divide_43(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
