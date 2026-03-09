"""Module 235: arithmetic helpers."""

def max_235(a, b):
    return a if a > b else b

def divide_235(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def add_235(a, b):
    return a + b

def modulo_235(a, b):
    return a % b
