"""Module 12: arithmetic helpers."""

def max_12(a, b):
    return a if a > b else b

def modulo_12(a, b):
    return a % b

def add_12(a, b):
    return a + b

def divide_12(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
