"""Module 128: arithmetic helpers."""

def modulo_128(a, b):
    return a % b

def subtract_128(a, b):
    return a - b

def divide_128(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_128(a, b):
    return a if a > b else b
