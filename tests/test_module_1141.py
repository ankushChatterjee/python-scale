"""Tests for test module 1141 — covers src modules [4561, 4562, 4563, 4564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4561 import add_4561
from module_4562 import subtract_4562
from module_4563 import multiply_4563
from module_4564 import divide_4564

def test_add_4561():
    assert add_4561(2, 3) == 5

def test_subtract_4562():
    assert subtract_4562(10, 4) == 6

def test_multiply_4563():
    assert multiply_4563(3, 7) == 21

def test_divide_4564():
    assert divide_4564(10, 2) == 5.0
