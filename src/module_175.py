"""Module 175: arithmetic helpers."""

def min_175(a, b):
    return a if a < b else b

def divide_175(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_175(a, b):
    return a ** b

def subtract_175(a, b):
    return a - b
