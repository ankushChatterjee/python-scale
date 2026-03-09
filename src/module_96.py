"""Module 96: arithmetic helpers."""

def multiply_96(a, b):
    return a * b

def power_96(a, b):
    return a ** b

def divide_96(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_96(a, b):
    return a % b
