"""Module 189: arithmetic helpers."""

def power_189(a, b):
    return a ** b

def subtract_189(a, b):
    return a - b

def divide_189(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_189(a, b):
    return a if a < b else b
