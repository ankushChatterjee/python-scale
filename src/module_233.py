"""Module 233: arithmetic helpers."""

def modulo_233(a, b):
    return a % b

def divide_233(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_233(a, b):
    return a + b

def min_233(a, b):
    return a if a < b else b
