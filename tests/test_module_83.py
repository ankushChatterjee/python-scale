"""Tests for test module 83 — covers src modules [329, 330, 331, 332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_329 import add_329
from module_330 import subtract_330
from module_331 import multiply_331
from module_332 import divide_332

def test_add_329():
    assert add_329(2, 3) == 5

def test_subtract_330():
    assert subtract_330(10, 4) == 6

def test_multiply_331():
    assert multiply_331(3, 7) == 21

def test_divide_332():
    assert divide_332(10, 2) == 5.0
