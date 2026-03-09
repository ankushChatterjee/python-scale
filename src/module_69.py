"""Module 69: arithmetic helpers."""

def add_69(a, b):
    return a + b

def divide_69(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_69(a, b):
    return a * b

def min_69(a, b):
    return a if a < b else b
