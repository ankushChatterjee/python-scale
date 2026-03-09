"""Tests for test module 2083 — covers src modules [8329, 8330, 8331, 8332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8329 import add_8329
from module_8330 import subtract_8330
from module_8331 import multiply_8331
from module_8332 import divide_8332

def test_add_8329():
    assert add_8329(2, 3) == 5

def test_subtract_8330():
    assert subtract_8330(10, 4) == 6

def test_multiply_8331():
    assert multiply_8331(3, 7) == 21

def test_divide_8332():
    assert divide_8332(10, 2) == 5.0
