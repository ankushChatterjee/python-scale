"""Module 187: arithmetic helpers."""

def modulo_187(a, b):
    return a % b

def divide_187(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_187(a, b):
    return a - b

def min_187(a, b):
    return a if a < b else b
