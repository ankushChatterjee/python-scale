"""Module 117: arithmetic helpers."""

def power_117(a, b):
    return a ** b

def divide_117(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_117(a, b):
    return a % b

def max_117(a, b):
    return a if a > b else b
