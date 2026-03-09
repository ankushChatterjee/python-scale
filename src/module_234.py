"""Module 234: arithmetic helpers."""

def modulo_234(a, b):
    return a % b

def power_234(a, b):
    return a ** b

def divide_234(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_234(a, b):
    return a * b
