"""Module 153: arithmetic helpers."""

def min_153(a, b):
    return a if a < b else b

def divide_153(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b

def modulo_153(a, b):
    return a % b

def add_153(a, b):
    return a + b
