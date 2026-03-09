"""Tests for test module 1895 — covers src modules [7577, 7578, 7579, 7580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7577 import add_7577
from module_7578 import subtract_7578
from module_7579 import multiply_7579
from module_7580 import divide_7580

def test_add_7577():
    assert add_7577(2, 3) == 5

def test_subtract_7578():
    assert subtract_7578(10, 4) == 6

def test_multiply_7579():
    assert multiply_7579(3, 7) == 21

def test_divide_7580():
    assert divide_7580(10, 2) == 5.0
