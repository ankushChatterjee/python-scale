"""Module 103: arithmetic helpers."""

def power_103(a, b):
    return a ** b

def min_103(a, b):
    return a if a < b else b

def modulo_103(a, b):
    return a % b

def divide_103(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
