"""Module 181: arithmetic helpers."""

def add_181(a, b):
    return a + b

def min_181(a, b):
    return a if a < b else b

def divide_181(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_181(a, b):
    return a ** b
