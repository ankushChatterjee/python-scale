"""Tests for test module 569 — covers src modules [2273, 2274, 2275, 2276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2273 import add_2273
from module_2274 import subtract_2274
from module_2275 import multiply_2275
from module_2276 import divide_2276

def test_add_2273():
    assert add_2273(2, 3) == 5

def test_subtract_2274():
    assert subtract_2274(10, 4) == 6

def test_multiply_2275():
    assert multiply_2275(3, 7) == 21

def test_divide_2276():
    assert divide_2276(10, 2) == 5.0
