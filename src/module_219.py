"""Module 219: arithmetic helpers."""

def max_219(a, b):
    return a if a > b else b

def divide_219(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_219(a, b):
    return a * b

def modulo_219(a, b):
    return a % b
