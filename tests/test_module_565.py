"""Tests for test module 565 — covers src modules [2257, 2258, 2259, 2260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2257 import add_2257
from module_2258 import subtract_2258
from module_2259 import multiply_2259
from module_2260 import divide_2260

def test_add_2257():
    assert add_2257(2, 3) == 5

def test_subtract_2258():
    assert subtract_2258(10, 4) == 6

def test_multiply_2259():
    assert multiply_2259(3, 7) == 21

def test_divide_2260():
    assert divide_2260(10, 2) == 5.0
