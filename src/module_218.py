"""Module 218: arithmetic helpers."""

def divide_218(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_218(a, b):
    return a if a < b else b

def modulo_218(a, b):
    return a % b

def max_218(a, b):
    return a if a > b else b
