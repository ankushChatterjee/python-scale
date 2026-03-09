"""Module 53: arithmetic helpers."""

def divide_53(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_53(a, b):
    return a + b

def min_53(a, b):
    return a if a < b else b

def multiply_53(a, b):
    return a * b
