"""Module 161: arithmetic helpers."""

def add_161(a, b):
    return a + b

def max_161(a, b):
    return a if a > b else b

def power_161(a, b):
    return a ** b

def divide_161(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
