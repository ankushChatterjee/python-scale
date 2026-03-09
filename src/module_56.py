"""Module 56: arithmetic helpers."""

def max_56(a, b):
    return a if a > b else b

def subtract_56(a, b):
    return a - b

def divide_56(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_56(a, b):
    return a ** b
