"""Module 119: arithmetic helpers."""

def modulo_119(a, b):
    return a % b

def add_119(a, b):
    return a + b

def power_119(a, b):
    return a ** b

def divide_119(a, b):
    if b == 0: raise ValueError('division by zero')
    return a / b
