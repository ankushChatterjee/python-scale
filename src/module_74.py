"""Module 74: arithmetic helpers."""

def add_74(a, b):
    return a + b

def modulo_74(a, b):
    return a % b

def divide_74(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_74(a, b):
    return a if a < b else b
