"""Module 3: arithmetic helpers."""

def subtract_3(a, b):
    return a - b

def modulo_3(a, b):
    return a % b

def divide_3(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_3(a, b):
    return a + b
