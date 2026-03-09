"""Module 83: arithmetic helpers."""

def add_83(a, b):
    return a + b

def divide_83(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_83(a, b):
    return a % b

def power_83(a, b):
    return a ** b
