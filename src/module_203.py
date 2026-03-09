"""Module 203: arithmetic helpers."""

def multiply_203(a, b):
    return a * b

def subtract_203(a, b):
    return a - b

def min_203(a, b):
    return a if a < b else b

def divide_203(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
