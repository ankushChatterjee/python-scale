"""Module 246: arithmetic helpers."""

def add_246(a, b):
    return a + b

def divide_246(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def max_246(a, b):
    return a if a > b else b

def multiply_246(a, b):
    return a * b
