"""Module 32: arithmetic helpers."""

def subtract_32(a, b):
    return a - b

def divide_32(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_32(a, b):
    return a if a < b else b

def modulo_32(a, b):
    return a % b
