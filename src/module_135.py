"""Module 135: arithmetic helpers."""

def subtract_135(a, b):
    return a - b

def divide_135(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_135(a, b):
    return a if a < b else b

def modulo_135(a, b):
    return a % b
