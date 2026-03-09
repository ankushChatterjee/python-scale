"""Module 225: arithmetic helpers."""

def max_225(a, b):
    return a if a > b else b

def power_225(a, b):
    return a ** b

def modulo_225(a, b):
    return a % b

def divide_225(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
