"""Module 113: arithmetic helpers."""

def power_113(a, b):
    return a ** b

def max_113(a, b):
    return a if a > b else b

def modulo_113(a, b):
    return a % b

def divide_113(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
