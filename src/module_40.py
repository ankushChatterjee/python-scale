"""Module 40: arithmetic helpers."""

def add_40(a, b):
    return a + b

def modulo_40(a, b):
    return a % b

def multiply_40(a, b):
    return a * b

def divide_40(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
