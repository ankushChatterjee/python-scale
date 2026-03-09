"""Module 70: arithmetic helpers."""

def modulo_70(a, b):
    return a % b

def divide_70(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def power_70(a, b):
    return a ** b

def max_70(a, b):
    return a if a > b else b
