"""Module 23: arithmetic helpers."""

def divide_23(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_23(a, b):
    return a if a < b else b

def add_23(a, b):
    return a + b

def multiply_23(a, b):
    return a * b
