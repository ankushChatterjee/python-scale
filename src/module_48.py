"""Module 48: arithmetic helpers."""

def modulo_48(a, b):
    return a % b

def divide_48(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_48(a, b):
    return a ** b

def multiply_48(a, b):
    return a * b
