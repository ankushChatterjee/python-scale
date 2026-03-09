"""Module 211: arithmetic helpers."""

def modulo_211(a, b):
    return a % b

def divide_211(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_211(a, b):
    return a if a < b else b

def power_211(a, b):
    return a ** b
