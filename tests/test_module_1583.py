"""Tests for test module 1583 — covers src modules [6329, 6330, 6331, 6332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6329 import add_6329
from module_6330 import subtract_6330
from module_6331 import multiply_6331
from module_6332 import divide_6332

def test_add_6329():
    assert add_6329(2, 3) == 5

def test_subtract_6330():
    assert subtract_6330(10, 4) == 6

def test_multiply_6331():
    assert multiply_6331(3, 7) == 21

def test_divide_6332():
    assert divide_6332(10, 2) == 5.0
