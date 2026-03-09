"""Module 78: arithmetic helpers."""

def divide_78(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_78(a, b):
    return a % b

def min_78(a, b):
    return a if a < b else b

def add_78(a, b):
    return a + b
