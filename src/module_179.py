"""Module 179: arithmetic helpers."""

def power_179(a, b):
    return a ** b

def modulo_179(a, b):
    return a % b

def divide_179(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_179(a, b):
    return a * b
