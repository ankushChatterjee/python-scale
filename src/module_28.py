"""Module 28: arithmetic helpers."""

def modulo_28(a, b):
    return a % b

def power_28(a, b):
    return a ** b

def max_28(a, b):
    return a if a > b else b

def divide_28(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
