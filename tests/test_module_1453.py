"""Tests for test module 1453 — covers src modules [5809, 5810, 5811, 5812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5809 import add_5809
from module_5810 import subtract_5810
from module_5811 import multiply_5811
from module_5812 import divide_5812

def test_add_5809():
    assert add_5809(2, 3) == 5

def test_subtract_5810():
    assert subtract_5810(10, 4) == 6

def test_multiply_5811():
    assert multiply_5811(3, 7) == 21

def test_divide_5812():
    assert divide_5812(10, 2) == 5.0
