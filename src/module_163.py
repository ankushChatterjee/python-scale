"""Module 163: arithmetic helpers."""

def add_163(a, b):
    return a + b

def multiply_163(a, b):
    return a * b

def divide_163(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_163(a, b):
    return a if a < b else b
