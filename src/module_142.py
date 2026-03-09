"""Module 142: arithmetic helpers."""

def power_142(a, b):
    return a ** b

def min_142(a, b):
    return a if a < b else b

def divide_142(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_142(a, b):
    return a % b
