"""Module 31: arithmetic helpers."""

def multiply_31(a, b):
    return a * b

def power_31(a, b):
    return a ** b

def subtract_31(a, b):
    return a - b

def divide_31(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
