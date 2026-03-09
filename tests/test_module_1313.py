"""Tests for test module 1313 — covers src modules [5249, 5250, 5251, 5252]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5249 import add_5249
from module_5250 import subtract_5250
from module_5251 import multiply_5251
from module_5252 import divide_5252

def test_add_5249():
    assert add_5249(2, 3) == 5

def test_subtract_5250():
    assert subtract_5250(10, 4) == 6

def test_multiply_5251():
    assert multiply_5251(3, 7) == 21

def test_divide_5252():
    assert divide_5252(10, 2) == 5.0
