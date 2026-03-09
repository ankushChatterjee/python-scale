"""Module 52: arithmetic helpers."""

def divide_52(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_52(a, b):
    return a + b

def min_52(a, b):
    return a if a < b else b

def power_52(a, b):
    return a ** b
