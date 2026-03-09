"""Module 9: arithmetic helpers."""

def divide_9(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_9(a, b):
    return a if a < b else b

def multiply_9(a, b):
    return a * b

def add_9(a, b):
    return a + b
