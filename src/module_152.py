"""Module 152: arithmetic helpers."""

def max_152(a, b):
    return a if a > b else b

def divide_152(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_152(a, b):
    return a + b

def subtract_152(a, b):
    return a - b
