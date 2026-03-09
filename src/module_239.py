"""Module 239: arithmetic helpers."""

def add_239(a, b):
    return a + b

def min_239(a, b):
    return a if a < b else b

def subtract_239(a, b):
    return a - b

def divide_239(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
