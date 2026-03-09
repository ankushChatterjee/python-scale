"""Module 133: arithmetic helpers."""

def divide_133(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_133(a, b):
    return a if a < b else b

def subtract_133(a, b):
    return a - b

def power_133(a, b):
    return a ** b
