"""Module 245: arithmetic helpers."""

def modulo_245(a, b):
    return a % b

def power_245(a, b):
    return a ** b

def divide_245(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_245(a, b):
    return a if a > b else b
