"""Module 26: arithmetic helpers."""

def min_26(a, b):
    return a if a < b else b

def power_26(a, b):
    return a ** b

def divide_26(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_26(a, b):
    return a - b
