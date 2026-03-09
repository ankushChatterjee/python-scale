"""Module 250: arithmetic helpers."""

def power_250(a, b):
    return a ** b

def modulo_250(a, b):
    return a % b

def divide_250(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_250(a, b):
    return a if a > b else b
