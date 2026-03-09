"""Tests for test module 2063 — covers src modules [8249, 8250, 8251, 8252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8249 import add_8249
from module_8250 import subtract_8250
from module_8251 import multiply_8251
from module_8252 import divide_8252

def test_add_8249():
    assert add_8249(2, 3) == 5

def test_subtract_8250():
    assert subtract_8250(10, 4) == 6

def test_multiply_8251():
    assert multiply_8251(3, 7) == 21

def test_divide_8252():
    assert divide_8252(10, 2) == 5.0
