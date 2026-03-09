"""Module 148: arithmetic helpers."""

def divide_148(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_148(a, b):
    return a * b

def min_148(a, b):
    return a if a < b else b

def power_148(a, b):
    return a ** b
