"""Module 68: arithmetic helpers."""

def min_68(a, b):
    return a if a < b else b

def add_68(a, b):
    return a + b

def subtract_68(a, b):
    return a - b

def divide_68(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
