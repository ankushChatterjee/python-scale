"""Module 196: arithmetic helpers."""

def modulo_196(a, b):
    return a % b

def subtract_196(a, b):
    return a - b

def divide_196(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_196(a, b):
    return a if a < b else b
