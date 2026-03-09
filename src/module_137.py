"""Module 137: arithmetic helpers."""

def max_137(a, b):
    return a if a > b else b

def divide_137(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_137(a, b):
    return a - b

def power_137(a, b):
    return a ** b
