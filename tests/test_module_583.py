"""Tests for test module 583 — covers src modules [2329, 2330, 2331, 2332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2329 import add_2329
from module_2330 import subtract_2330
from module_2331 import multiply_2331
from module_2332 import divide_2332

def test_add_2329():
    assert add_2329(2, 3) == 5

def test_subtract_2330():
    assert subtract_2330(10, 4) == 6

def test_multiply_2331():
    assert multiply_2331(3, 7) == 21

def test_divide_2332():
    assert divide_2332(10, 2) == 5.0
