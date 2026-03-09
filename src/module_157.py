"""Module 157: arithmetic helpers."""

def min_157(a, b):
    return a if a < b else b

def divide_157(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_157(a, b):
    return a + b

def max_157(a, b):
    return a if a > b else b
