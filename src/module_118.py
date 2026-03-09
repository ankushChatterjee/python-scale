"""Module 118: arithmetic helpers."""

def subtract_118(a, b):
    return a - b

def divide_118(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_118(a, b):
    return a % b

def max_118(a, b):
    return a if a > b else b
