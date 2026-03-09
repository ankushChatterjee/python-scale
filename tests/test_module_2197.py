"""Tests for test module 2197 — covers src modules [8785, 8786, 8787, 8788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8785 import add_8785
from module_8786 import subtract_8786
from module_8787 import multiply_8787
from module_8788 import divide_8788

def test_add_8785():
    assert add_8785(2, 3) == 5

def test_subtract_8786():
    assert subtract_8786(10, 4) == 6

def test_multiply_8787():
    assert multiply_8787(3, 7) == 21

def test_divide_8788():
    assert divide_8788(10, 2) == 5.0
