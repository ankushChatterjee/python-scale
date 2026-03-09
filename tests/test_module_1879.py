"""Tests for test module 1879 — covers src modules [7513, 7514, 7515, 7516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7513 import add_7513
from module_7514 import subtract_7514
from module_7515 import multiply_7515
from module_7516 import divide_7516

def test_add_7513():
    assert add_7513(2, 3) == 5

def test_subtract_7514():
    assert subtract_7514(10, 4) == 6

def test_multiply_7515():
    assert multiply_7515(3, 7) == 21

def test_divide_7516():
    assert divide_7516(10, 2) == 5.0
