"""Module 155: arithmetic helpers."""

def modulo_155(a, b):
    return a % b

def min_155(a, b):
    return a if a < b else b

def divide_155(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_155(a, b):
    return a ** b
