"""Tests for test module 141 — covers src modules [561, 562, 563, 564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_561 import add_561
from module_562 import subtract_562
from module_563 import multiply_563
from module_564 import divide_564

def test_add_561():
    assert add_561(2, 3) == 5

def test_subtract_562():
    assert subtract_562(10, 4) == 6

def test_multiply_563():
    assert multiply_563(3, 7) == 21

def test_divide_564():
    assert divide_564(10, 2) == 5.0
