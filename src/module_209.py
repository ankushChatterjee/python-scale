"""Module 209: arithmetic helpers."""

def modulo_209(a, b):
    return a % b

def power_209(a, b):
    return a ** b

def subtract_209(a, b):
    return a - b

def divide_209(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
