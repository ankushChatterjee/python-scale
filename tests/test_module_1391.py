"""Tests for test module 1391 — covers src modules [5561, 5562, 5563, 5564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5561 import add_5561
from module_5562 import subtract_5562
from module_5563 import multiply_5563
from module_5564 import divide_5564

def test_add_5561():
    assert add_5561(2, 3) == 5

def test_subtract_5562():
    assert subtract_5562(10, 4) == 6

def test_multiply_5563():
    assert multiply_5563(3, 7) == 21

def test_divide_5564():
    assert divide_5564(10, 2) == 5.0
