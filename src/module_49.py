"""Module 49: arithmetic helpers."""

def max_49(a, b):
    return a if a > b else b

def modulo_49(a, b):
    return a % b

def divide_49(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_49(a, b):
    return a + b
