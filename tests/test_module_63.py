"""Tests for test module 63 — covers src modules [249, 250, 251, 252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_249 import add_249
from module_250 import subtract_250
from module_251 import multiply_251
from module_252 import divide_252

def test_add_249():
    assert add_249(2, 3) == 5

def test_subtract_250():
    assert subtract_250(10, 4) == 6

def test_multiply_251():
    assert multiply_251(3, 7) == 21

def test_divide_252():
    assert divide_252(10, 2) == 5.0
