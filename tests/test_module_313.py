"""Tests for test module 313 — covers src modules [1249, 1250, 1251, 1252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1249 import add_1249
from module_1250 import subtract_1250
from module_1251 import multiply_1251
from module_1252 import divide_1252

def test_add_1249():
    assert add_1249(2, 3) == 5

def test_subtract_1250():
    assert subtract_1250(10, 4) == 6

def test_multiply_1251():
    assert multiply_1251(3, 7) == 21

def test_divide_1252():
    assert divide_1252(10, 2) == 5.0
