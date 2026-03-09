"""Module 170: arithmetic helpers."""

def multiply_170(a, b):
    return a * b

def subtract_170(a, b):
    return a - b

def min_170(a, b):
    return a if a < b else b

def divide_170(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
