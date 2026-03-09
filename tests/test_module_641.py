"""Tests for test module 641 — covers src modules [2561, 2562, 2563, 2564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2561 import add_2561
from module_2562 import subtract_2562
from module_2563 import multiply_2563
from module_2564 import divide_2564

def test_add_2561():
    assert add_2561(2, 3) == 5

def test_subtract_2562():
    assert subtract_2562(10, 4) == 6

def test_multiply_2563():
    assert multiply_2563(3, 7) == 21

def test_divide_2564():
    assert divide_2564(10, 2) == 5.0
