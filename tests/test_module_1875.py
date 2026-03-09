"""Tests for test module 1875 — covers src modules [7497, 7498, 7499, 7500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7497 import add_7497
from module_7498 import subtract_7498
from module_7499 import multiply_7499
from module_7500 import divide_7500

def test_add_7497():
    assert add_7497(2, 3) == 5

def test_subtract_7498():
    assert subtract_7498(10, 4) == 6

def test_multiply_7499():
    assert multiply_7499(3, 7) == 21

def test_divide_7500():
    assert divide_7500(10, 2) == 5.0
