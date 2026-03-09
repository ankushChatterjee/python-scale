"""Module 6: arithmetic helpers."""

def min_6(a, b):
    return a if a < b else b

def subtract_6(a, b):
    return a - b

def divide_6(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_6(a, b):
    return a % b
