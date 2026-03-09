"""Tests for test module 555 — covers src modules [2217, 2218, 2219, 2220]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2217 import add_2217
from module_2218 import subtract_2218
from module_2219 import multiply_2219
from module_2220 import divide_2220

def test_add_2217():
    assert add_2217(2, 3) == 5

def test_subtract_2218():
    assert subtract_2218(10, 4) == 6

def test_multiply_2219():
    assert multiply_2219(3, 7) == 21

def test_divide_2220():
    assert divide_2220(10, 2) == 5.0
