"""Module 160: arithmetic helpers."""

def add_160(a, b):
    return a + b

def divide_160(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_160(a, b):
    return a % b

def power_160(a, b):
    return a ** b
