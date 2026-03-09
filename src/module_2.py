"""Module 2: arithmetic helpers."""

def divide_2(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def subtract_2(a, b):
    return a - b

def min_2(a, b):
    return a if a < b else b

def add_2(a, b):
    return a + b
