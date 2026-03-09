"""Module 81: arithmetic helpers."""

def divide_81(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_81(a, b):
    return a * b

def max_81(a, b):
    return a if a > b else b

def subtract_81(a, b):
    return a - b
