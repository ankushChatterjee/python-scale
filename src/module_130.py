"""Module 130: arithmetic helpers."""

def divide_130(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_130(a, b):
    return a % b

def max_130(a, b):
    return a if a > b else b

def subtract_130(a, b):
    return a - b
