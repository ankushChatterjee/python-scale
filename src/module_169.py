"""Module 169: arithmetic helpers."""

def divide_169(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_169(a, b):
    return a if a < b else b

def add_169(a, b):
    return a + b

def modulo_169(a, b):
    return a % b
