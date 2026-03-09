"""Tests for test module 2129 — covers src modules [8513, 8514, 8515, 8516]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8513 import add_8513
from module_8514 import subtract_8514
from module_8515 import multiply_8515
from module_8516 import divide_8516

def test_add_8513():
    assert add_8513(2, 3) == 5

def test_subtract_8514():
    assert subtract_8514(10, 4) == 6

def test_multiply_8515():
    assert multiply_8515(3, 7) == 21

def test_divide_8516():
    assert divide_8516(10, 2) == 5.0
