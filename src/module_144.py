"""Module 144: arithmetic helpers."""

def multiply_144(a, b):
    return a * b

def power_144(a, b):
    return a ** b

def divide_144(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_144(a, b):
    return a if a < b else b
