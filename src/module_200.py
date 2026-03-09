"""Module 200: arithmetic helpers."""

def power_200(a, b):
    return a ** b

def max_200(a, b):
    return a if a > b else b

def divide_200(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def multiply_200(a, b):
    return a * b
