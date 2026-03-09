"""Module 241: arithmetic helpers."""

def min_241(a, b):
    return a if a < b else b

def power_241(a, b):
    return a ** b

def divide_241(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_241(a, b):
    return a + b
