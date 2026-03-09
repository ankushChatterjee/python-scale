"""Module 79: arithmetic helpers."""

def subtract_79(a, b):
    return a - b

def divide_79(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_79(a, b):
    return a ** b

def modulo_79(a, b):
    return a % b
