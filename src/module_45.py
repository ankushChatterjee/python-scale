"""Module 45: arithmetic helpers."""

def multiply_45(a, b):
    return a * b

def power_45(a, b):
    return a ** b

def divide_45(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_45(a, b):
    return a % b
