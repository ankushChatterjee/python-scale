"""Module 224: arithmetic helpers."""

def subtract_224(a, b):
    return a - b

def max_224(a, b):
    return a if a > b else b

def add_224(a, b):
    return a + b

def divide_224(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
