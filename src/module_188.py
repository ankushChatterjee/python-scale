"""Module 188: arithmetic helpers."""

def min_188(a, b):
    return a if a < b else b

def multiply_188(a, b):
    return a * b

def add_188(a, b):
    return a + b

def divide_188(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
