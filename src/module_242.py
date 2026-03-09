"""Module 242: arithmetic helpers."""

def max_242(a, b):
    return a if a > b else b

def multiply_242(a, b):
    return a * b

def divide_242(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def min_242(a, b):
    return a if a < b else b
